from fastapi import FastAPI

from app.backend.entrypoints.controllers.document_controller import (
    router as document_router,
)
from app.backend.entrypoints.controllers.search_controller import (
    router as search_router,
)
from app.backend.entrypoints.controllers.embeddings_controller import (
    router as embedding_router,
)

app = FastAPI(
    title="RAG Semantic Search API",
    description="API for semantic search using RAG (Retrieval-Augmented Generation)",
)

app.include_router(document_router)
app.include_router(search_router)
app.include_router(embedding_router)
