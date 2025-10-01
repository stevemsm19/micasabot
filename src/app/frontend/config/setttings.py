from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    backend_api_base_url: str = "http://localhost:8001/api"
    documents_endpoint: str = "/documents/add"
    search_endpoint: str = "/documents/search"

    model_config = SettingsConfigDict(env_file=".env")

@lru_cache()
def get_settings() -> Settings:
    return Settings()