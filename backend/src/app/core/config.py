from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Text Summarization API"
    
    # Model settings
    MODEL_NAME: str = "gemma2"
    MAX_LENGTH: int = 500
    MIN_LENGTH: int = 100
    
    class Config:
        case_sensitive = True
        env_file = ".env"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
