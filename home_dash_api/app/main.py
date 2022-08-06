from app.config import Settings, get_settings
from fastapi import Depends, FastAPI

app = FastAPI()


@app.get("/ping")
async def ping(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong",
        "enviroment": settings.enviroment,
        "testing": settings.testing,
    }
