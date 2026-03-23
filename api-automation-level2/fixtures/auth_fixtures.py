import pytest
from services.auth_service import AuthService

@pytest.fixture(scope="session")
def auth_token():
    service = AuthService()

    payload = {
        "email": "admin@test.com",
        "password": "password"
    }

    response = service.login(payload)

    return response.json().get("access_token")