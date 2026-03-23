from services.user_service import UserService

def test_admin_access(auth_token):
    service = UserService()
    res = service.get_users(auth_token)
    assert res.status_code == 200