from utils.http_client import HttpClient
from config.endpoints import TASKS

client = HttpClient()

class TaskService:

    def create_task(self, token, data):
        return client.request("POST", TASKS, token=token, json=data)