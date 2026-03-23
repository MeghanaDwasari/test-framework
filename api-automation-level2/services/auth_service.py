from utils.http_client import HttpClient
from config.endpoints import AUTH

client = HttpClient()

class AuthService:

    def register(self, data):
        return client.request("POST", f"{AUTH}/register", json=data)

    def login(self, data):
        return client.request("POST", f"{AUTH}/login", json=data)