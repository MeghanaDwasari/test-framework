import pytest
import json

@pytest.fixture(scope="session")
def test_data():
    with open("config/test_data.json") as f:
        return json.load(f)