from flask_login import UserMixin

from db_factory import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    deposit = db.Column(db.Integer, default=0)
    role = db.Column(db.String(10))
