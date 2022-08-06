import os

from app.config import Settings, get_settings
from fastapi import Depends, FastAPI
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

register_tortoise(
    app,
    db_url=os.environ.get("DATABASE_URL"),
    modules={"models": ["app.models.user"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get("/ping")
async def ping(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong",
        "enviroment": settings.enviroment,
        "testing": settings.testing,
    }
