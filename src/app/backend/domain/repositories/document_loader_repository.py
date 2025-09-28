from abc import ABC, abstractmethod
from typing import List
from app.backend.domain.entities.document import Document
from fastapi import UploadFile


class DocumentLoaderRepository(ABC):
    @abstractmethod
    async def load_documents(self, file_paths: List[UploadFile]) -> List[Document]:
        pass
