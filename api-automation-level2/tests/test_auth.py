import pytest
from services.auth_service import AuthService
from utils.schema_validator import validate_schema
import json

service = AuthService()

def test_valid_login(test_data):
    res = service.login(test_data["valid_user"])
    assert res.status_code == 200

    schema = json.load(open("config/api_schemas.json"))["login_response"]
    validate_schema(res.json(), schema)

@pytest.mark.parametrize("data", [
    {"email": "wrong@test.com", "password": "wrong"},
    {"email": "", "password": ""},
])
def test_invalid_login(data):
    res = service.login(data)
    assert res.status_code in [400, 401]