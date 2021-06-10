import logging
import os

from fastapi import FastAPI
from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import register_tortoise

log = logging.getLogger("uvicorn")


def init_db(app: FastAPI) -> None:
    # This register tortoise to fastapi App
    register_tortoise(
        app,
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=False,  # set to false to not create the schema each time we restart the app
        add_exception_handlers=True,
    )


# add a generate schema function
async def generate_schema() -> None:
    log.info("Initializing Tortoise...")

    await Tortoise.init(
        db_url=os.environ.get("DATABASE_URL"), modules={"models": ["models.tortoise"]}
    )

    log.info("Generating database schema via Tortoise...")
    await Tortoise.generate_schemas()  # generate schema
    await Tortoise.close_connections()  # close connection


if __name__ == "__main__":
    # create executable to be able to run this file only once!
    run_async(generate_schema())
