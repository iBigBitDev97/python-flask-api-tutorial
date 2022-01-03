from flask import Flask
app = Flask(__name__)
from flask import Flask, jsonify
from flask import request

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    global todos
    todos.append(request.json)
    return jsonify({"data": todos}), 200 








if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)