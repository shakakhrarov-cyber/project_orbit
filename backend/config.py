import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Database
    database_url: str = os.getenv("DATABASE_URL", "postgresql://orbit:orbit_dev@localhost:5432/orbit_db")
    
    # Redis
    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379")
    
    # OpenAI (for future use)
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    
    # App
    app_name: str = "ORBIT"
    debug: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    class Config:
        env_file = ".env"

settings = Settings()

