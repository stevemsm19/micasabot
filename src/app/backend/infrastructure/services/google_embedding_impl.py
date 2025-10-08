from typing import List
from google import genai

from app.backend.domain.services.embedding_service import EmbeddingService

class GoogleEmbeddingServiceImpl(EmbeddingService):
    def __init__(self, api_key: str, model: str):
        self.client = genai.Client(api_key=api_key)
        self.model = model

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        all_embeddings = []
        for i in range(0, len(texts), 100):
            batch = texts[i:i + 100]
            response = self.client.models.embed_content(model=self.model, contents=batch)
            all_embeddings.extend([e.values for e in response.embeddings])
        return all_embeddings
    
    def embed_query(self, text: str) -> List[float]:
        response = self.client.models.embed_content(model=self.model, contents=[text])
        return response.embeddings[0].values
