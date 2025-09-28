from typing import List
from app.backend.domain.repositories.vector_store_repository import VectorStoreRepository
from app.backend.domain.repositories.document_loader_repository import DocumentLoaderRepository
from app.backend.domain.services.llm_service import LLMService
from app.backend.domain.services.text_splitter_service import TextSplitterService
from app.backend.domain.entities.query import QueryResult

class DocumentService:
    def __init__(
        self,
        document_repository: VectorStoreRepository,
        pdf_repository: DocumentLoaderRepository,
        text_splitter: TextSplitterService,
        llm_service: LLMService
    ):
        self.document_repository = document_repository
        self.pdf_repository = pdf_repository
        self.text_splitter = text_splitter
        self.llm_service = llm_service
    
    async def add_document_from_uploads(self, file_paths: List[str]) -> dict:
        try:
            pages = await self.pdf_repository.load_documents(file_paths)
            
            chunks = self.text_splitter.split_documents(pages)
            

            document_ids = await self.document_repository.add_document(chunks)
            
            return {
                "message": "Documents added successfully",
                "total_pages": len(pages),
                "total_chunks": len(chunks),
                "document_ids_sample": document_ids[:3]
            }
        except Exception as e:
            raise Exception(f"Error adding documents: {str(e)}")
    
    async def search_and_answer(self, question: str) -> QueryResult:
        try:
            context_chunks = await self.document_repository.search_similar(question, n_results=3)
        
            context = "\n\n".join([chunk.content for chunk in context_chunks])
            
            answer = await self.llm_service.generate_answer(context, question)

            print(context)
            
            return QueryResult(
                answer=answer,
                context=context_chunks,
                question=question
            )
        except Exception as e:
            raise Exception(f"Error searching documents: {str(e)}")