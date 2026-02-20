# Fault-Tolerant Distributed Task Scheduler

A Python-based distributed task scheduler that supports:

- Job queuing using Redis
- Automatic retries on failure
- Local load balancing across multiple workers
- REST API to submit tasks

---

## **Features**

- Fault-tolerant: Failed tasks automatically retry
- Distributed: Multiple workers can process tasks simultaneously
- Scalable: Add more worker nodes for higher throughput
- Simple REST API for job submission

---

## **Tech Stack**

- Python 3.11+
- Flask
- Celery
- Redis
- Gunicorn (for deployment)

---
