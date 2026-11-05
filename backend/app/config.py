from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import model_validator

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str = "postgresql+psycopg://user:password@localhost:5432/mini_blog"
    secret_key: str = "change-me"
    environment: Literal["development", "test", "production"] = "development"
    app_name: str = "Mini-Blog"


settings = Settings()