from flask import Blueprint, jsonify
print('api-ing')
api = Blueprint('api', __name__, url_prefix='/api/v1')
print('api-ed')
HARDCODED_TODOS = [{
    "id": 1,
    "title": "Watch CSSE6400 Lecture",
    "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
    "completed": True,
    "deadline_at": "2023-02-27T00:00:00",
    "created_at": "2023-02-20T00:00:00",
    "updated_at": "2023-02-20T00:00:00"
}]

@api.route('/health')
def health():
    return jsonify({'status': 'ok'})
print('def-ed health')
@api.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(HARDCODED_TODOS)

@api.route('/todos/<int:id>', methods=['GET'])
def get_todo(id):
    return jsonify(HARDCODED_TODOS[0])

@api.route('/todos', methods=['POST'])
def create_todo():
    #TODO: This todo method
    return jsonify(HARDCODED_TODOS[0])

@api.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    #TODO: This todo method
    return jsonify(HARDCODED_TODOS[0])


@api.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    #TODO: This todo method
    return jsonify(HARDCODED_TODOS[0])


