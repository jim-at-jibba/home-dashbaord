import logging

from app.api import ping, recipes, user
from app.db import init_db
from fastapi import FastAPI

log = logging.getLogger("uvicorn")


def create_application():
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(user.user_router)
    application.include_router(recipes.recipe_router)

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Startup event")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
