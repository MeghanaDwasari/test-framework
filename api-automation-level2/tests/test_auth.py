import pytest
import json
import allure
from services.auth_service import AuthService
from utils.schema_validator import validate_schema

service = AuthService()


@allure.feature("Authentication")
@allure.story("Valid Login")
def test_valid_login(test_data):
    res = service.login({
        "email": "real_admin@email.com",
        "password": "real_password"
    })
    assert res.status_code == 200


@allure.feature("Authentication")
@allure.story("Invalid Login")
@pytest.mark.parametrize("data", [
    {"email": "wrong@test.com", "password": "wrong"},
    {"email": "", "password": ""},
])
def test_invalid_login(data):
    res = service.login(data)

    with allure.step("Verify invalid login response"):
        assert res.status_code in (400, 401)
