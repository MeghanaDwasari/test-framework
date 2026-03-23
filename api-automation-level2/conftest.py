import pytest
import json
from services.auth_service import AuthService

@pytest.fixture
def auth_token():
    service = AuthService()
    res = service.login({
        "email": "admin@test.com",
        "password": "password"
    })
    return res.json().get("access_token")

@pytest.fixture
def test_data():
    with open("config/test_data.json") as f:
        return json.load(f)