from typing import List

from langchain_chroma import Chroma
from langchain_core.documents import Document

from app.backend.domain.repositories.vector_store_repository import (
    VectorStoreRepository,
)

class ChromaRepositoryImpl(VectorStoreRepository):
    def __init__(self, vector_store: Chroma):
        self.vector_store = vector_store

    async def add_document(self, documents: List[Document]) -> List[str]:
        document_ids = self.vector_store.add_documents(documents=documents)
        return document_ids

    from typing import List


    async def search_similar(
        self, query: str, num_results: int, similarity_threshold: float
    ) -> List[Document]:
        results = self.vector_store.similarity_search_with_score(query, num_results)

        chunks: List[Document] = []

        for doc, score in results:
            if score <= similarity_threshold:
                doc_with_score = Document(
                    page_content=doc.page_content,
                    metadata={**doc.metadata, "score": score}
                )
                chunks.append(doc_with_score)

        return chunks
