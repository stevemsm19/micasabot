from typing import List
from app.backend.domain.entities.document import DocumentChunk


class QueryResult:
    def __init__(self, question: str, answer: str, context: List[DocumentChunk]):
        self.answer: str = answer
        self.context: List[DocumentChunk] = context
        self.question: str = question
