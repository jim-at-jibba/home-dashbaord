from app.config import Settings, get_settings
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/ping")
async def ping(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.enviroment,
        "testing": settings.testing,
    }
