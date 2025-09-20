from abc import ABC, abstractmethod
from typing import List
from app.backend.domain.entities.document import Document, DocumentChunk

class TextSplitterService(ABC):
    @abstractmethod
    def split_documents(self, documents: List[Document]) -> List[DocumentChunk]:
        pass