from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    print(data)
    new_task = Task(id=task_id_control, title=data.get("title"), description=data.get("description"))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "New Task successfully added!"})




if __name__ == "__main__":
    app.run(debug=True)