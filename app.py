from flask import Flask , request , jsonify
from redis import Redis
from rq import Queue
from tasks import * 
import os

def creat_app():
    app = Flask(__name__)


    redis_conn = Redis()
    queue = Queue(connection=redis_conn, default_timeout=None)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    task_map = {
        "reverse_text": reverse_text,
        "uppercase": uppercase,
        "sum_numbers": sum_numbers
    }

    @app.route('/tasks',methods=["POST"])
    def creat_task():
        data = request.json
        task_type = data.get("task_type")
        input = data.get("data")
        job = queue.enqueue(task_map[task_type], input, job_timeout=None)
        return jsonify({
            "task_id": job.id,
            "status": "queued"
        }), 202
        
    @app.route('/results/<task_id>',methods=["GET"])
    def get_results(task_id):
        job = queue.fetch_job(task_id)
        if not job:
            return jsonify({"error": "Task Not Found"}), 404
        return jsonify({
            "task_id" : task_id,
            "status" : job.get_status(),
            "result" : job.result
        })

    @app.route('/queue',methods=["GET"])
    def get_queue():
        return jsonify({"queued jons" : [job.id for job in queue.jobs]})
    
    @app.route('/results',methods=["GET"])
    def get_all_reuslts():
        jobs = queue.jobs
        completed = []
        for job in jobs:
            if job.is_finished:
                completed.append({
                    "task_id" : job.get_id(),
                    "result" : job.result
                })
        return jsonify(completed)

    return app

    
if __name__ == "__main__":
    app = creat_app()
    app.run(debug=True)