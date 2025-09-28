from fastapi import FastAPI
from app.backend.entrypoints.controllers.document_controller import (
    router as document_router,
)

app = FastAPI(
    title="RAG Semantic Search API",
    description="API for semantic search using RAG (Retrieval-Augmented Generation)",
)

app.include_router(document_router)
