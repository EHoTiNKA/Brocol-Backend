import logging

from fastapi import FastAPI
from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import register_tortoise


log = logging.getLogger("uvicorn")

# TORTOISE_ORM = {
#     "connections": {"default": "sqlite://db.sqlite3"},
#     "apps": {
#         ""
#     }
# } 

def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url="sqlite://db.sqlite3",
        modules={"models": ["app.models"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )

async def generate_schema() -> None:
    log.info("Initializing Tortoise...")

    await Tortoise.init(
        db_url="sqlite://db.sqlite3",
        modules={"models": ["app.models"]},
    )
    log.info("Generating database schema via Tortoise...")
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()


if __name__ == "__main__":
    run_async(generate_schema())
    