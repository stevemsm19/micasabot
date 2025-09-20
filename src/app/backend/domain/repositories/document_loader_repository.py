from abc import ABC, abstractmethod
from typing import List
from app.backend.domain.entities.document import Document

class DocumentLoaderRepository(ABC):
    @abstractmethod
    async def load_documents(self, file_paths: List[str]) -> List[Document]:
        pass