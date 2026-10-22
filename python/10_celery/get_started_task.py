from celery import Celery

app = Celery(
    "get_started_task",
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0"
)

@app.task
def addition(a, b):
    return a + b