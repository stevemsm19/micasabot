from typing import List

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document as LangchainDocument

from app.backend.domain.entities.document_entity import DocumentEntity
from app.backend.domain.services.text_splitter_service import TextSplitterService

class RecursiveTextSplitterImpl(TextSplitterService):
    def __init__(self, chunk_size: int, chunk_overlap: int):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    def split_documents(self, documents: List[DocumentEntity]) -> List[DocumentEntity]:
        langchain_docs = [
            LangchainDocument(
                page_content=doc.content,
                metadata=doc.metadata
            ) for doc in documents
        ]
        
        split_langchain_docs = self.text_splitter.split_documents(langchain_docs)
        
        split_entities = [
            DocumentEntity(
                content=doc.page_content,
                metadata=doc.metadata
            ) for doc in split_langchain_docs
        ]
        
        return split_entities