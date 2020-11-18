from flask import Blueprint
from controllers.web.TodoController import TodoController
from controllers.web.UserController import UserController
from flask_login import login_required, current_user

# Rotas principais
web = Blueprint('web', __name__)

@web.route('/')
@login_required
def index():
  return TodoController.index()

@web.route('/create', methods=['POST'])
@login_required
def create():
  return TodoController.create()

@web.route('/update/<int:id>', methods=['POST'])
@login_required
def update(id):
  return TodoController.update(id)

@web.route('/delete/<int:id>')
@login_required
def delete(id):
  return TodoController.delete(id)

@web.route('/complete/<int:id>')
@login_required
def complete(id):
  return TodoController.complete(id)

# Rotas de autenticação
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
  return UserController.login()

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
  return UserController.signup()

@auth.route('/logout')
@login_required
def logout():
  return UserController.logout()