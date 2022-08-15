import os

import pytest
from app.config import Settings, get_settings
from app.main import create_application
from starlette.testclient import TestClient


def get_settings_override():
    return Settings(testing=True, database_url=os.environ.get("DATABASE_TEST_URL"))


@pytest.fixture(scope="module")
def test_app():
    app = create_application()
    # setup
    # dependency_overrides is a dict of key/value pairs where the key is the
    # dependency name and the value is what we'd like to override it with
    app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(app) as test_client:

        # testing
        yield test_client
