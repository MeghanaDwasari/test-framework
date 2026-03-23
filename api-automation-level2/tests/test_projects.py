from services.project_service import ProjectService

def test_create_project(auth_token):
    service = ProjectService()
    res = service.create_project(auth_token, {"name": "Test Project"})
    assert res.status_code == 201