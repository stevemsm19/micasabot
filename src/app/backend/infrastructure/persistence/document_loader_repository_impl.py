import os
from typing import List

from fastapi import HTTPException

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document as LangchainDocument

from app.backend.domain.repositories.document_loader_repository import DocumentLoaderRepository
from app.backend.domain.entities.document_entity import DocumentEntity

class DocumentLoaderRepositoryImpl(DocumentLoaderRepository):
    def __init__(self, upload_dir: str):
        self.upload_dir = upload_dir

    def _save_file(self, filename: str, content: bytes) -> str:
        if not filename:
            raise HTTPException(
                status_code=400, detail="Uploaded file must have a filename"
            )

        try:
            os.makedirs(self.upload_dir, exist_ok=True)
            file_path = os.path.join(self.upload_dir, filename)

            with open(file_path, "wb") as f:
                f.write(content)

            return file_path
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error saving file: {str(e)}")

    async def _load_pdf(self, file_path: str) -> List[DocumentEntity]:
        loader = PyPDFLoader(file_path)
        entities: List[DocumentEntity] = []

        async for page in loader.alazy_load():
            relative_source = file_path.split("temp_files/")[-1] if "temp_files/" in file_path else file_path
            page_number = page.metadata.get("page_label") or page.metadata.get("page")

            entity = DocumentEntity(
                content=page.page_content, 
                metadata={"source": relative_source, "page": page_number}
            )
            entities.append(entity)

        return entities

    def _load_txt(self, file_path: str) -> List[DocumentEntity]:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            
            entity = DocumentEntity(
                content=content, 
                metadata={"source": file_path}
            )
            return [entity]
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error loading TXT: {str(e)}")

    async def load_documents(self, file_data: List[dict]) -> List[DocumentEntity]:
        saved_file_paths = []
        for file_info in file_data:
            file_path = self._save_file(file_info['filename'], file_info['content'])
            saved_file_paths.append(file_path)

        entities: List[DocumentEntity] = []
        for file_path in saved_file_paths:
            if file_path.endswith(".pdf"):
                docs = await self._load_pdf(file_path)
            elif file_path.endswith(".txt"):
                docs = self._load_txt(file_path)
            else:
                raise HTTPException(status_code=400, detail="Unsupported file format")
            entities.extend(docs)

        return entities