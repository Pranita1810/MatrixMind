import os
import time
from celery import Celery

app = Celery(
    "task",
    broker=os.getenv(
        "CELERY_BROKER_URL",
        "redis://127.0.0.1:6379/0"
    ),
    backend=os.getenv(
        "CELERY_RESULT_BACKEND",
        "redis://127.0.0.1:6379/0"
    )
)

@app.task
def process_data():
    return {"Data": "Transforming Data"}