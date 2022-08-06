import logging
import os
from functools import lru_cache

from pydantic import AnyUrl, BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    enviroment: str = os.environ.get("ENVIRONMENT", "development")
    testing: bool = os.environ.get("TESTING", False)
    database_url: AnyUrl = os.environ.get("DATABASE_URL")


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Getting settings")
    return Settings()
