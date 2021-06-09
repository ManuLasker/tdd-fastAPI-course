import os
from typing import Generator
import pytest
from starlette.testclient import TestClient
from tortoise.contrib.fastapi import register_tortoise
from app.main import create_app
from app.config import get_settings, Settings


def get_settings_override() -> Settings:
    return Settings(testing=1, database_url=os.environ.get("DATABASE_TEST_URL"))


@pytest.fixture(scope="module")
def test_app() -> Generator:
    # set up
    # override app dependencei get_settings with test settings define previously
    app = create_app()
    app.dependency_overrides[get_settings] = get_settings_override
    
    with TestClient(app) as test_client:
        # testing
        yield test_client
    # tear down

@pytest.fixture(scope="module")
def test_app_with_db() -> Generator:
    # set up
    app = create_app()
    app.dependency_overrides[get_settings] = get_settings_override
    register_tortoise(
        app,
        db_url=get_settings_override().database_url,
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=True,
        add_exception_handlers=True
    )
    # create test client
    with TestClient(app) as test_client:
        yield test_client
    # tear down