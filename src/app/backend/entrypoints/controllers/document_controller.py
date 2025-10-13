from typing import List
from fastapi import HTTPException, UploadFile, File, APIRouter, Depends

from app.backend.application.services.document_service import DocumentService
from app.backend.application.dtos.document_dtos import (
    DocumentFileDTO,
    AddDocumentsResponseDTO,
)

from app.backend.config.dependencies import get_document_service

router = APIRouter(prefix="/documents", tags=["documents"])


@router.post("/add")
async def add_document(
    files: List[UploadFile] = File(...),
    document_service: DocumentService = Depends(get_document_service),
) -> AddDocumentsResponseDTO:

    document_file_dtos = []
    for f in files:
        if f.filename is None:
            raise HTTPException(status_code=400, detail="File must have a filename")
        document_file_dtos.append(
            DocumentFileDTO(filename=f.filename, content=await f.read())
        )

    result_dto = await document_service.add_document_from_uploads(document_file_dtos)

    return AddDocumentsResponseDTO(
        total_pages=result_dto.total_pages, total_chunks=result_dto.total_chunks
    )
