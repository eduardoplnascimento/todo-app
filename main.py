import os
from flask import Flask
from database import db
from routes.Web import web
from routes.Web import auth
from routes.Api import api
from flask_login import LoginManager
from models.User import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SECRET_KEY'] = 'secret'

app.register_blueprint(web)
app.register_blueprint(auth)
app.register_blueprint(api, url_prefix='/api')

db.init_app(app)

with app.app_context():
  db.create_all()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)