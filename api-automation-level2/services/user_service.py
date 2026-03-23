from utils.http_client import HttpClient
from config.endpoints import USERS

client = HttpClient()

class UserService:

    def get_users(self, token):
        return client.request("GET", USERS, token=token)

    def create_user(self, token, data):
        return client.request("POST", USERS, token=token, json=data)