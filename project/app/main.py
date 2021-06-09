import os
from fastapi import FastAPI, Depends
from app.config import get_settings, Settings
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

# This register tortoise models and initialize db to fastapi
register_tortoise(
    app,
    db_url=get_settings().database_url,
    modules={"models": ["app.models.tortoise"]},
    generate_schemas=True,
    add_exception_handlers=True
)

@app.get("/ping")
async def ping(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong",
        "environment": settings.environment,
        "testing": settings.testing,
    }
