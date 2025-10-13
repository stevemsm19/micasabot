from fastapi import APIRouter, Depends

from app.backend.application.dtos.embedding_dtos import EmbeddingsResponseDTO
from app.backend.application.services.embedding_service import EmbeddingService

from app.backend.config.dependencies import get_embedding_service

router = APIRouter(tags=["embeddings"])


@router.get("/embeddings")
async def get_embeddings(
    limit: int | None = None,
    embedding_service: EmbeddingService = Depends(get_embedding_service),
) -> EmbeddingsResponseDTO:

    data = await embedding_service.get_embeddings()
    embeddings = data["embeddings"]
    metadatas = data["metadatas"]

    total = len(embeddings)
    dim = len(embeddings[0]) if total > 0 else 0

    if limit is not None:
        embeddings = embeddings[:limit]
        metadatas = metadatas[:limit]

    return EmbeddingsResponseDTO(
        total_embeddings=total,
        embedding_dimension=dim,
        embeddings=embeddings,
        metadatas=metadatas,
    )
