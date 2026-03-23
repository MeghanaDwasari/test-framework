from services.auth_service import AuthService

def test_empty_payload():
    service = AuthService()
    res = service.login({})
    assert res.status_code in [400, 401]

def test_large_payload():
    service = AuthService()
    data = {"email": "a"*1000, "password": "b"*1000}
    res = service.login(data)
    assert res.status_code in [400, 401]