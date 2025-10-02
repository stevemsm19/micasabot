from abc import ABC, abstractmethod
from typing import List
from app.backend.domain.entities.document_entity import DocumentEntity

class DocumentLoaderRepository(ABC):
    @abstractmethod
    async def load_documents(self, file_data: List[dict]) -> List[DocumentEntity]:
        pass