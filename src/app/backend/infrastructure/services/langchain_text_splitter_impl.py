from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.backend.domain.services.text_splitter_service import TextSplitterService
from app.backend.domain.entities.document import Document, DocumentChunk

class RecursiveTextSplitterImpl(TextSplitterService):
    def __init__(self, chunk_size: int, chunk_overlap: int):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def split_documents(self, documents: List[Document]) -> List[DocumentChunk]:

        all_splits = self.text_splitter.split_documents(documents)

        chunks = []
        for split in all_splits:
            chunk = DocumentChunk(
                content=split.page_content,
                metadata=split.metadata,
            )
            chunks.append(chunk)

        return chunks
