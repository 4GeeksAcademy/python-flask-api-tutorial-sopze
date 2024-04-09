from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def todos_get():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("TODO: store request data: ", request_body)
    todos.append(request_body)
    json_text = jsonify(todos)
    return json_text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    max= len(todos)
    if position >= max:
        position= max-1
    del todos[position]
    json_text = jsonify(todos)
    return json_text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)