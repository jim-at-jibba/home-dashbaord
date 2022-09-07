import logging
import os

from fastapi import FastAPI
from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import register_tortoise

log = logging.getLogger("uvicorn")

TORTOISE_ORM = {
    "connections": {"default": os.environ.get("DATABASE_URL")},
    "apps": {
        "models": {
            "models": [
                "app.models.user",
                "aerich.models",
                "app.models.recipes.recipe",
                "app.models.recipes.recipe_ingredients",
                "app.models.recipes.ingredient",
                "app.models.recipes.category",
                "app.models.recipes.measurement",
                "app.models.recipes.measurement_qty",
            ],
            "default_connection": "default",
        }
    },
}


def init_db(app: FastAPI) -> None:

    register_tortoise(
        app,
        db_url=os.environ.get("DATABASE_URL"),
        modules={
            "models": [
                "app.models.recipes.recipe",
                "app.models.recipes.recipe_ingredients",
                "app.models.recipes.ingredient",
                "app.models.recipes.category",
                "app.models.recipes.measurement",
                "app.models.recipes.measurement_qty",
            ]
        },
        generate_schemas=False,
        add_exception_handlers=True,
    )


async def generate_schemas() -> None:
    log.info("Iitializing database...")

    await Tortoise.init(
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["app.models.user", "app.models.recipes"]},
    )
    log.info("Generating database schema...")
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()


if __name__ == "__main__":
    run_async(generate_schemas())
