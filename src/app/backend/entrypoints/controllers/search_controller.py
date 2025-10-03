from fastapi import APIRouter, Depends

from app.backend.application.services.search_service import SearchService
from app.backend.application.dtos.search_dtos import SearchRequestDTO, SearchResponseDTO

from app.backend.config.dependencies import get_search_service

router = APIRouter(tags=["ask-question"])

@router.post("/ask-question") 
async def ask_question(
    request: SearchRequestDTO,
    search_service: SearchService = Depends(get_search_service),
) -> SearchResponseDTO:
    
    request_dto = SearchRequestDTO(
        question=request.question,
        num_results=request.num_results,
        similarity_threshold=request.similarity_threshold
    )
    
    result_dto = await search_service.search_and_answer(request_dto)
    
    return SearchResponseDTO(
        answer=result_dto.answer,
        context=result_dto.context,
        question=result_dto.question
    )