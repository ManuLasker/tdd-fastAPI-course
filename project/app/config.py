import logging
import os
from pydantic import BaseSettings
from functools import lru_cache

log = logging.getLogger("uvicorn") # get uvicorn logger

# settings class that takes values from environment variables
class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)

@lru_cache() # this will cache the result of this function
def get_settings() -> Settings:
    log.info("Loading config settings from the environment...")
    return Settings()