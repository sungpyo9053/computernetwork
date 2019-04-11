
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

#Flask 인스턴스 생성
app = Flask(__name__)
api = Api(app)

#할일 정의
TODOS = {
    'todo1': {'task': 'Make Money'},
    'todo2': {'task': 'Play PS4'},
    'todo3': {'task': 'Study!'},
}

#예외 처리
def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')

# 할일(Todo)
# Get, Delete, Put 정의
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


 if __name__ == '__main__':
            app.run(host='0.0.0.0', port=8888, debug=True)

# 할일 리스트(Todos)
# Get, POST 정의
