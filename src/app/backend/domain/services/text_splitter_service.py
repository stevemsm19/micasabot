from abc import ABC, abstractmethod
from typing import List
from app.backend.domain.entities.document_entity import DocumentEntity

class TextSplitterService(ABC):
    @abstractmethod
    def split_documents(self, documents: List[DocumentEntity]) -> List[DocumentEntity]:
        pass

