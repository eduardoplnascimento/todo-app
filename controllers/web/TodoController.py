from flask import render_template, request, redirect, url_for
from models.Todo import Todo, db
from flask_login import current_user

class TodoController():
  def index():
    todos = Todo.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', todos=todos)

  def create():
    title = request.form.get('title')
    new_todo = Todo(
      title=title, complete=False, user_id=current_user.id
    )
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('web.index'))

  def delete(id):
    todo = Todo.query.filter_by(id=id).first()
    if todo.user_id != current_user.id:
      return redirect(url_for('web.index'))
    
    if todo.complete != True:
      return redirect(url_for('web.index'))
      
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('web.index'))

  def complete(id):
    todo = Todo.query.filter_by(id=id).first()
    todo.complete = True
    db.session.commit()
    return redirect(url_for('web.index'))

  def update(id):
    title = request.form.get('title')
    todo = Todo.query.filter_by(id=id).first()
    todo.title = title
    db.session.commit()
    return redirect(url_for('web.index'))