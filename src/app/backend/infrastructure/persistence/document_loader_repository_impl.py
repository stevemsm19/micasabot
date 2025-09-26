import os
from typing import List
from fastapi import UploadFile, HTTPException
from langchain_community.document_loaders import PyPDFLoader
from app.backend.domain.entities.document import Document
from app.backend.domain.repositories.document_loader_repository import DocumentLoaderRepository

class DocumentLoaderRepositoryImpl(DocumentLoaderRepository):
    def __init__(self, upload_dir: str):
        self.upload_dir = upload_dir

    def save_file(self, file: UploadFile) -> str:
        try:
            os.makedirs(self.upload_dir, exist_ok=True)
            file_path = os.path.join(self.upload_dir, file.filename)

            with open(file_path, "wb") as f:
                f.write(file.file.read())

            return file_path
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error saving file: {str(e)}")

    async def load_pdf(self, file_path: str) -> List[Document]:
        loader = PyPDFLoader(file_path)
        pages = []
        async for page in loader.alazy_load():
            pages.append(
                Document(page_content=page.page_content, metadata={"source": file_path})
            )
        return pages

    def load_txt(self, file_path: str) -> List[Document]:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            return [Document(page_content=content, metadata={"source": file_path})]
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error loading TXT: {str(e)}")

    async def load_documents(self, files: List[UploadFile]) -> List[Document]:
        saved_file_paths = []
        for file in files:
            file_path = self.save_file(file)
            saved_file_paths.append(file_path)

        documents: List[Document] = []
        for file_path in saved_file_paths:
            if file_path.endswith(".pdf"):
                docs = await self.load_pdf(file_path)
            elif file_path.endswith(".txt"):
                docs = self.load_txt(file_path)
            else:
                raise HTTPException(status_code=400, detail="Unsupported file format")
            documents.extend(docs)

        return documents
