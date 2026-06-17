# conftest.py
import pytest
from fastapi.testclient import TestClient
from backend.main import app
from unittest.mock import patch

@pytest.fixture(scope='module')
def test_client():
    with TestClient(app) as client:
        yield client

@pytest.fixture(scope='module')
def mock_database():
    with patch('backend.database.get_db', return_value=None):
        yield
