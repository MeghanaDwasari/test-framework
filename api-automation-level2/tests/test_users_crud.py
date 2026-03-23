from services.user_service import UserService

def test_user_crud(auth_token):
    service = UserService()

    # CREATE
    res = service.create_user(auth_token, {
        "email": "new@test.com",
        "password": "password"
    })
    assert res.status_code == 201

    # READ
    res = service.get_users(auth_token)
    assert res.status_code == 200