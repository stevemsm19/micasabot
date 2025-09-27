from pydantic import BaseModel
from typing import List, Dict, Any


class AddDocumentsRequest(BaseModel):
    file_paths: List[str]


class AddDocumentsResponse(BaseModel):
    message: str
    total_pages: int
    total_chunks: int
    document_ids_sample: List[str]


class SearchRequest(BaseModel):
    question: str


class DocumentChunkResponse(BaseModel):
    content: str
    metadata: Dict[str, Any]
    score: float    


class SearchResponse(BaseModel):
    answer: str
    context: List[DocumentChunkResponse]
    question: str
