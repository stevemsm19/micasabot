from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
import os

class Settings(BaseSettings):
    backend_api_base_url: str = "http://localhost:8001/"

    model_config = SettingsConfigDict(env_file=os.path.join(os.path.dirname(__file__), "../.env"))

@lru_cache()
def get_settings() -> Settings:
    return Settings()