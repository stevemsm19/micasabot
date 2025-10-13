from app.backend.domain.repositories.vector_store_repository import (
    VectorStoreRepository,
)
from app.backend.domain.services.llm_service import LLMService

from app.backend.application.dtos.search_dtos import SearchRequestDTO, SearchResponseDTO


class SearchService:
    def __init__(
        self,
        vector_store_repository: VectorStoreRepository,
        llm_service: LLMService,
    ):
        self.vector_store_repository = vector_store_repository
        self.llm_service = llm_service

    async def search_and_answer(
        self, request_dto: SearchRequestDTO
    ) -> SearchResponseDTO:
        try:
            context_entities = await self.vector_store_repository.search_similar(
                request_dto.question,
                request_dto.num_results,
                request_dto.similarity_threshold,
            )

            context_responses = []
            for entity in context_entities:
                context_responses.append(
                    {
                        "content": entity.content,
                        "metadata": entity.metadata,
                    }
                )

            context = "\n\n".join([entity.content for entity in context_entities])
            answer = await self.llm_service.generate_answer(
                context, request_dto.question
            )

            return SearchResponseDTO(
                answer=answer,
                context=context_responses,
                question=request_dto.question,
            )

        except Exception as e:
            raise Exception(f"Error searching documents: {str(e)}")
