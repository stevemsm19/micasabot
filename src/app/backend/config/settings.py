from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    google_api_key: str = "YOUR_GOOGLE_API_KEY"
    gemini_model: str = "gemini-2.5-flash"
    embedding_model: str = "gemini-embedding-001"
    collection_name: str = "documents"
    chroma_host: str = "localhost"

    model_config = SettingsConfigDict(env_file=".env")
