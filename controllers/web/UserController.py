from flask import render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from models.User import User, db
from flask_login import login_user, logout_user

class UserController():
  def login():
    if request.method == 'GET':
      return render_template('login.html')

    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
      return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    return redirect(url_for('web.index'))

  def signup():
    if request.method == 'GET':
      return render_template('signup.html')

    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if user:
      return redirect(url_for('auth.signup'))

    new_user = User(
      email=email, name=name,
      password=generate_password_hash(password, method='sha256')
    )
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))

  def logout():
    logout_user()
    return redirect(url_for('web.index'))