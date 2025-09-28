import chromadb

from functools import lru_cache
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from app.backend.config.settings import Settings
from app.backend.application.services.document_service import DocumentService
from app.backend.infrastructure.persistence.document_loader_repository_impl import DocumentLoaderRepositoryImpl
from app.backend.infrastructure.persistence.chroma_repository_impl import (
    ChromaRepositoryImpl,
)
from app.backend.infrastructure.services.langchain_text_splitter_impl import (
    RecursiveTextSplitterImpl,
)
from app.backend.infrastructure.services.google_llm_service_impl import GoogleLLMServiceImpl

@lru_cache()
def get_settings() -> Settings:
    return Settings()

@lru_cache()
def get_embeddings():
    settings = get_settings()
    return HuggingFaceEmbeddings(model_name=settings.embedding_model)

@lru_cache()
def get_vector_store():
    settings = get_settings()
    embeddings = get_embeddings()

    client = chromadb.HttpClient(host="localhost", port=8000)  

    return Chroma(
        client=client,
        collection_name=settings.collection_name,
        embedding_function=embeddings
    )

def get_document_service() -> DocumentService:
    settings = get_settings()
    vector_store = get_vector_store()

    document_loader_repository = DocumentLoaderRepositoryImpl("temp_files")
    vector_store_repository = ChromaRepositoryImpl(vector_store)

    text_splitter = RecursiveTextSplitterImpl(
        chunk_size=1000, chunk_overlap=200
    )
    llm_service = GoogleLLMServiceImpl(
        api_key=settings.google_api_key, model=settings.gemini_model
    )

    return DocumentService(
        vector_store_repository=vector_store_repository,
        document_loader_repository=document_loader_repository,
        text_splitter=text_splitter,
        llm_service=llm_service,
    )
