from flask import Flask,jsonify,request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    jsn_list = jsonify(todos)
    return jsn_list, 200

@app.route('/todos', methods=['POST'])
def add_new_todo():
   global todos
   new_todo = request.json
   todos.append(new_todo)
   return jsonify(todos),201

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo():
    global todos
    delete_task = request.json
    todos.remove(position)
    return jsonify(todos),201

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)