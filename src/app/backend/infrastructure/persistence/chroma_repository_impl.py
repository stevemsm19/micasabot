from typing import List
from langchain_chroma import Chroma
from langchain_core.documents import Document as LangchainDocument
from app.backend.domain.repositories.vector_store_repository import (
    VectorStoreRepository,
)
from app.backend.domain.entities.document import DocumentChunk


class ChromaRepositoryImpl(VectorStoreRepository):
    def __init__(self, vector_store: Chroma):
        self.vector_store = vector_store

    async def add_document(self, documents: List[DocumentChunk]) -> List[str]:
        
        lc_documents = []
        for doc in documents:
            lc_doc = LangchainDocument(page_content=doc.content, metadata=doc.metadata)
            lc_documents.append(lc_doc)

        document_ids = self.vector_store.add_documents(documents=lc_documents)
        return document_ids

    async def search_similar(
        self, query: str, n_results: int = 3, similarity_threshold: float = 0.5
    ) -> List[DocumentChunk]:
        results = self.vector_store.similarity_search_with_score(query, n_results)

        chunks: List[DocumentChunk] = []

        for doc, score in results:
            if score <= similarity_threshold:
                chunk = DocumentChunk(
                    content=doc.page_content,
                    metadata=doc.metadata,
                    score=score,
                )
                chunks.append(chunk)

        return chunks
