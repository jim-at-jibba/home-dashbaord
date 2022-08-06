import logging
import os

from pydantic import BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    enviroment: str = os.getenv("ENVIROMENT", "development")
    testing: bool = os.getenv("TESTING", False)


def get_settings() -> BaseSettings:
    log.info("Getting settings")
    return Settings()
