from functools import lru_cache
from os import environ

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Application
    name: str = "App Name"
    version: str = "0.1"
    root_path: str = "/api/v1"
    DEBUG: bool = True

    # Application configuration
    env: str = environ.get("FASTAPI_ENV", "dev")

    model_config = SettingsConfigDict(
        env_prefix="APP_",
        env_file="./docker/.env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
