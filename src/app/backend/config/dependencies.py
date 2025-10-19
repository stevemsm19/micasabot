import chromadb

from functools import lru_cache
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from app.backend.config.settings import Settings

from app.backend.application.services.document_service import DocumentService
from app.backend.application.services.search_service import SearchService
from app.backend.application.services.embedding_service import EmbeddingService

from app.backend.infrastructure.persistence.document_loader_repository_impl import (
    DocumentLoaderRepositoryImpl,
)
from app.backend.infrastructure.persistence.chroma_repository_impl import (
    ChromaRepositoryImpl,
)
from app.backend.infrastructure.services.langchain_text_splitter_impl import (
    RecursiveTextSplitterImpl,
)
from app.backend.infrastructure.services.google_llm_service_impl import (
    GoogleLLMServiceImpl,
)

from app.backend.infrastructure.services.google_embedding_impl import (
    GoogleEmbeddingServiceImpl,
)
from app.backend.utils.constants import CHUNK_OVERLAP, CHUNK_SIZE


@lru_cache()
def get_settings() -> Settings:
    return Settings()


SETTINGS = get_settings()


@lru_cache()
def get_embeddings() -> GoogleEmbeddingServiceImpl:
    return GoogleEmbeddingServiceImpl(
        api_key=SETTINGS.google_api_key, model=SETTINGS.embedding_model
    )

@lru_cache()
def get_vector_store() -> Chroma:
    embeddings = get_embeddings()

    client = chromadb.HttpClient(host=SETTINGS.chroma_host, port=8000)

    client.get_or_create_collection(SETTINGS.collection_name)

    return Chroma(
        client=client,
        collection_name=SETTINGS.collection_name,
        embedding_function=embeddings,
    )


def get_document_service() -> DocumentService:
    vector_store = get_vector_store()

    document_loader_repository = DocumentLoaderRepositoryImpl(
        "src/app/backend/temp_files"
    )
    vector_store_repository = ChromaRepositoryImpl(vector_store)

    text_splitter = RecursiveTextSplitterImpl(
        chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP
    )

    return DocumentService(
        vector_store_repository=vector_store_repository,
        document_loader_repository=document_loader_repository,
        text_splitter=text_splitter,
    )


def get_search_service() -> SearchService:
    vector_store = get_vector_store()

    vector_store_repository = ChromaRepositoryImpl(vector_store)

    llm_service = GoogleLLMServiceImpl(
        api_key=SETTINGS.google_api_key, model=SETTINGS.gemini_model
    )

    return SearchService(
        vector_store_repository=vector_store_repository,
        llm_service=llm_service,
    )


def get_embedding_service() -> EmbeddingService:
    vector_store = get_vector_store()

    vector_store_repository = ChromaRepositoryImpl(vector_store)

    return EmbeddingService(vector_store_repository)
