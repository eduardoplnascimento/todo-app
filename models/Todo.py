from database import db
from sqlalchemy_serializer import SerializerMixin

class Todo(db.Model, SerializerMixin):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100))
  complete = db.Column(db.Boolean)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))