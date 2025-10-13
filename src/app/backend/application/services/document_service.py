from typing import Dict, List, Union

from app.backend.domain.repositories.vector_store_repository import (
    VectorStoreRepository,
)
from app.backend.domain.repositories.document_loader_repository import (
    DocumentLoaderRepository,
)
from app.backend.domain.services.text_splitter_service import TextSplitterService

from app.backend.application.dtos.document_dtos import (
    DocumentFileDTO,
    AddDocumentsResponseDTO,
)


class DocumentService:
    def __init__(
        self,
        vector_store_repository: VectorStoreRepository,
        document_loader_repository: DocumentLoaderRepository,
        text_splitter: TextSplitterService,
    ):
        self.vector_store_repository = vector_store_repository
        self.document_loader_repository = document_loader_repository
        self.text_splitter = text_splitter

    async def add_document_from_uploads(
        self, file_dtos: List[DocumentFileDTO]
    ) -> AddDocumentsResponseDTO:
        try:

            file_data: List[Dict[str, Union[bytes, str]]] = [
                {"filename": dto.filename, "content": dto.content} for dto in file_dtos
            ]

            documents = await self.document_loader_repository.load_documents(file_data)

            chunks = self.text_splitter.split_documents(documents)

            await self.vector_store_repository.add_document(chunks)

            return AddDocumentsResponseDTO(
                total_pages=len(documents), total_chunks=len(chunks)
            )
        except Exception as e:
            raise Exception(f"Error adding documents: {str(e)}")
