broker_url = "redis://localhost:6379/0"
result_backend = "redis://localhost:6379/1"

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'UTC'
enable_utc = True

# Retry defaults
task_default_retry_delay = 5  # seconds
task_annotations = {'*': {'max_retries': 3}}
