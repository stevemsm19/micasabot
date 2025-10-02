from typing import List

from app.backend.domain.repositories.vector_store_repository import VectorStoreRepository
from app.backend.domain.repositories.document_loader_repository import DocumentLoaderRepository

from app.backend.domain.services.llm_service import LLMService
from app.backend.domain.services.text_splitter_service import TextSplitterService

from app.backend.application.dtos.document_dtos import DocumentFileDTO, AddDocumentsResponseDTO
from app.backend.application.dtos.search_dtos import SearchRequestDTO, SearchResponseDTO

class DocumentService:
    def __init__(
        self,
        vector_store_repository: VectorStoreRepository,
        document_loader_repository: DocumentLoaderRepository,
        text_splitter: TextSplitterService,
        llm_service: LLMService,
    ):
        self.vector_store_repository = vector_store_repository
        self.document_loader_repository = document_loader_repository
        self.text_splitter = text_splitter
        self.llm_service = llm_service

    async def add_document_from_uploads(
        self, 
        file_dtos: List[DocumentFileDTO]
    ) -> AddDocumentsResponseDTO:
        try:
            
            file_data = [{'filename': dto.filename, 'content': dto.content} for dto in file_dtos]

            documents = await self.document_loader_repository.load_documents(file_data)

            chunks = self.text_splitter.split_documents(documents)

            await self.vector_store_repository.add_document(chunks)

            return AddDocumentsResponseDTO(
                total_pages=len(documents),
                total_chunks=len(chunks)
            )
        except Exception as e:
            raise Exception(f"Error adding documents: {str(e)}")

    async def search_and_answer(self, request_dto: SearchRequestDTO) -> SearchResponseDTO:
        try:
            context_entities = await self.vector_store_repository.search_similar(
                request_dto.question, 
                request_dto.num_results, 
                request_dto.similarity_threshold
            )

            context_responses = []
            for entity in context_entities:
                context_responses.append({
                    "content": entity.content, 
                    "metadata": entity.metadata,
                })

            context = "\n\n".join([entity.content for entity in context_entities]) 
            answer = await self.llm_service.generate_answer(context, request_dto.question)

            return SearchResponseDTO(
                answer=answer,
                context=context_responses,
                question=request_dto.question,
            )
        
        except Exception as e:
            raise Exception(f"Error searching documents: {str(e)}")