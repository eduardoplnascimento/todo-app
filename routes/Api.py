from flask import Blueprint
from controllers.api.TodoController import TodoController

api = Blueprint('api', __name__)

@api.route('/')
def index():
  return TodoController.index()

@api.route('/create', methods=['POST'])
def create():
  return TodoController.create()

@api.route('/update/<int:id>', methods=['POST'])
def update(id):
  return TodoController.update(id)

@api.route('/delete/<int:id>')
def delete(id):
  return TodoController.delete(id)

@api.route('/complete/<int:id>')
def complete(id):
  return TodoController.complete(id)