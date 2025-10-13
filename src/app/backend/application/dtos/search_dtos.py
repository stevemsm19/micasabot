from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class SearchRequestDTO:
    question: str
    num_results: int
    similarity_threshold: float


@dataclass
class SearchResponseDTO:
    answer: str
    context: List[Dict[str, Any]]
    question: str
