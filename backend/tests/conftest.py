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

# Add the following lines to address the human's feedback
from backend.diagnostic import encrypt_log
import os

@pytest.fixture(scope='module')
def encrypted_diagnostic_log():
    log_path = 'diagnostic/logd.log'
    if not os.path.exists(log_path):
        encrypt_log()
    yield log_path