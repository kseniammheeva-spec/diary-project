"""Фикстуры для тестов."""
import pytest
from app import app as flask_app


@pytest.fixture
def app():
    """Тестовое приложение."""
    flask_app.config.update(TESTING=True)
    yield flask_app


@pytest.fixture
def client(app):
    """Flask test client."""
    return app.test_client()