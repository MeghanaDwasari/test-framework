from utils.http_client import HttpClient
from config.endpoints import PROJECTS

client = HttpClient()

class ProjectService:

    def create_project(self, token, data):
        return client.request("POST", PROJECTS, token=token, json=data)