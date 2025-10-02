from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class SearchRequestDTO:
    question: str
    num_results: int = 4
    similarity_threshold: float = 0.5

@dataclass
class SearchResponseDTO:
    answer: str
    context: List[Dict[str, Any]]
    question: str