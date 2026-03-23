from services.api_lab_service import ApiLabService

def test_status_codes():
    service = ApiLabService()

    for code in [200, 201, 400, 500]:
        res = service.get_status(code)
        assert res.status_code == code