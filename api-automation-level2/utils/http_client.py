import requests
from config.settings import BASE_URL, API_TIMEOUT

class HttpClient:

    def request(self, method, endpoint, token=None, **kwargs):
        url = BASE_URL + endpoint
        headers = kwargs.get("headers", {})

        if token:
            headers["Authorization"] = f"Bearer {token}"

        response = requests.request(
            method,
            url,
            headers=headers,
            timeout=API_TIMEOUT,
            **kwargs
        )

        return response