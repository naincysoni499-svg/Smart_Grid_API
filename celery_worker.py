from celery import Celery

celery = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    include=["tasks"]      # <-- Add this line
)

celery.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"]
)
