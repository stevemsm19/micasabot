from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class EmbeddingsResponseDTO:
    total_embeddings: int
    embedding_dimension: int
    embeddings: List[List[float]]
    metadatas: List[Dict[str, Any]]
