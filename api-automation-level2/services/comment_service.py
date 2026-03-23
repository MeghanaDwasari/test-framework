from utils.http_client import HttpClient
from config.endpoints import COMMENTS

client = HttpClient()

class CommentService:

    def add_comment(self, token, data):
        return client.request("POST", COMMENTS, token=token, json=data)