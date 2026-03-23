import pytest
import json
import allure
from services.auth_service import AuthService
from utils.schema_validator import validate_schema

service = AuthService()


@allure.feature("Authentication")
@allure.story("Valid Login")
def test_valid_login(test_data):
    res = service.login(test_data["admin"])

    with allure.step("Verify status code"):
        assert res.status_code == 200

    with allure.step("Validate response schema"):
        with open("config/api_schemas.json") as f:
            schema = json.load(f)["login_response"]
        validate_schema(res.json(), schema)


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
