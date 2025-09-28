from fastapi import UploadFile, File, APIRouter, HTTPException, Depends
from typing import Dict, Any

from app.backend.application.services.document_service import DocumentService
from app.backend.application.schemas.document_schemas import (
    SearchRequest,
    SearchResponse,
    DocumentChunkResponse,
)
from app.backend.config.dependencies import get_document_service

router = APIRouter(prefix="/api", tags=["documents"])


@router.post("/documents/add")
async def add_document(
    files: list[UploadFile] = File(...),
    document_service: DocumentService = Depends(get_document_service),
) -> Dict[str, Any]:
    try:
        result = await document_service.add_document_from_uploads(files)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/documents/search", response_model=SearchResponse)
async def search_documents(
    request: SearchRequest,
    document_service: DocumentService = Depends(get_document_service),
) -> SearchResponse:
    try:
        result = await document_service.search_and_answer(request.question)

        context_responses = []
        for chunk in result.context:
            score = chunk.score if chunk.score is not None else 0.0
            context_responses.append(
                DocumentChunkResponse(
                    content=chunk.content, metadata=chunk.metadata, score=score
                )
            )

        return SearchResponse(
            answer=result.answer, context=context_responses, question=result.question
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
