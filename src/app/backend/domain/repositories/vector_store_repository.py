# app/backend/domain/repositories/vector_store_repository.py
from abc import ABC, abstractmethod
from typing import List
from app.backend.domain.entities.document_entity import DocumentEntity

class VectorStoreRepository(ABC):
    @abstractmethod
    async def add_document(self, documents: List[DocumentEntity]) -> List[str]:
        pass

    @abstractmethod
    async def search_similar(
        self, 
        query: str, 
        num_results: int, 
        similarity_threshold: float
    ) -> List[DocumentEntity]:
        pass