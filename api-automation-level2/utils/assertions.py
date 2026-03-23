def assert_status_code(response, expected):
    assert response.status_code == expected, f"Expected {expected}, got {response.status_code}"

def assert_key_exists(response_json, key):
    assert key in response_json, f"{key} not found in response"