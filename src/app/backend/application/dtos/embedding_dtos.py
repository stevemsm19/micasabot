from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class EmbeddingsResponseDTO:
    total_embeddings: int
    total_documents: int
    embedding_dimension: int
    embeddings: List[List[float]]
    metadatas: List[Dict[str, Any]]
