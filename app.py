from flask import Flask, request, jsonify
from tasks import process_job

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_job():
    data = request.json
    job_id = data.get('job_id')
    if not job_id:
        return jsonify({"error": "job_id required"}), 400

    task = process_job.delay(job_id)
    return jsonify({"message": f"Job {job_id} submitted", "task_id": task.id})

if __name__ == '__main__':
    app.run(debug=True)
