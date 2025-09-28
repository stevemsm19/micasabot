from abc import ABC, abstractmethod
from typing import List
from app.backend.domain.entities.document import DocumentChunk


class VectorStoreRepository(ABC):
    @abstractmethod
    async def add_document(self, documents: List[DocumentChunk]) -> List[str]:
        pass

    @abstractmethod
    async def search_similar(
        self, query: str, n_results: int, similarity_threshold: float
    ) -> List[DocumentChunk]:
        pass
