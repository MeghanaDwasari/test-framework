import pytest
import json
import allure
from services.auth_service import AuthService
from utils.schema_validator import validate_schema

service = AuthService()


@allure.feature("Authentication")
@allure.story("Valid Login")
def test_valid_login(test_data):
    # ✅ Use data from test_data.json
    user = test_data["valid_user"]

    res = service.login({
        "email": user["email"],
        "password": user["password"]
    })

    with allure.step("Verify status code"):
        assert res.status_code == 200

    # ✅ Optional: validate schema
    with allure.step("Validate response schema"):
        schema = json.load(open("config/api_schemas.json"))["login_response"]
        validate_schema(res.json(), schema)


@allure.feature("Authentication")
@allure.story("Invalid Login")
@pytest.mark.parametrize("data", [
    {"email": "wrong@test.com", "password": "wrong"},
    {"email": "", "password": ""}
])
def test_invalid_login(data):
    res = service.login(data)

    with allure.step("Verify invalid login response"):
        # ✅ Correct assertion
        assert res.status_code in (400, 401)
