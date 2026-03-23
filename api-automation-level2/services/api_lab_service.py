from utils.http_client import HttpClient
from config.endpoints import API_LAB

client = HttpClient()

class ApiLabService:

    def get_status(self, code):
        return client.request("GET", f"{API_LAB}/status/{code}")