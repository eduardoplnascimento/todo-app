from flask import request, jsonify
from models.Todo import Todo, db

class TodoController():
  def index():
    query = Todo.query.all()
    todos = [item.to_dict() for item in query]
    return jsonify(
      {
        'success': True,
        'data': todos,
        'error': None
      }
    )
  
  def create():
    title = request.json['title']
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return jsonify(
      {
        'success': True,
        'data': new_todo.to_dict(),
        'error': None
      }
    )

  def delete(id):
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return jsonify(
      {
        'success': True,
        'data': None,
        'error': None
      }
    )

  def complete(id):
    todo = Todo.query.filter_by(id=id).first()
    todo.complete = True
    db.session.commit()
    return jsonify(
      {
        'success': True,
        'data': todo.to_dict(),
        'error': None
      }
    )

  def update(id):
    title = request.json['title']
    todo = Todo.query.filter_by(id=id).first()
    todo.title = title
    db.session.commit()
    return jsonify(
      {
        'success': True,
        'data': todo.to_dict(),
        'error': None
      }
    )
