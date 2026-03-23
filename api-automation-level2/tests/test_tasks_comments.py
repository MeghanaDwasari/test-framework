from services.task_service import TaskService
from services.comment_service import CommentService

def test_task_and_comments(auth_token):
    task_service = TaskService()
    comment_service = CommentService()

    task = task_service.create_task(auth_token, {"title": "Task"})
    assert task.status_code == 201

    comment = comment_service.add_comment(auth_token, {"text": "Nice"})
    assert comment.status_code == 201