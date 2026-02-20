from celery import Celery
from celery.exceptions import Retry
import random
import time

app = Celery('tasks')
app.config_from_object('celeryconfig')

@app.task(bind=True, max_retries=3)
def process_job(self, job_id):
    try:
        print(f"Processing Job {job_id}")
        # Simulate random failure
        if random.random() < 0.3:
            raise ValueError("Random Failure Occurred")
        time.sleep(2)  # Simulate work
        print(f"Job {job_id} Completed Successfully")
        return f"Job {job_id} done"
    except Exception as exc:
        print(f"Job {job_id} failed, retrying...")
        raise self.retry(exc=exc)
