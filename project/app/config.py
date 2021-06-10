import logging
import os
from functools import lru_cache

from pydantic import AnyUrl, BaseSettings

log = logging.getLogger("uvicorn")  # get uvicorn logger


class Settings(BaseSettings):
    # settings class that takes values from environment variables

    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)
    database_url: AnyUrl = os.environ.get("DATABASE_URL")


@lru_cache()  # this will cache the result of this function
def get_settings() -> Settings:
    log.info("Loading config settings from the environment...")
    return Settings()
