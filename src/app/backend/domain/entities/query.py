from typing import List
from app.backend.domain.entities.document import DocumentChunk
class QueryResult:
    def __init__(self, question, answer: str, context: List[DocumentChunk]):
        self.answer = answer
        self.context = context
        self.question = question