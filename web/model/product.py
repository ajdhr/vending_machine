from sqlalchemy import ForeignKey

from db_factory import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    cost = db.Column(db.Integer)
    amount_available = db.Column(db.Integer)
    seller_id = db.Column(db.Integer, ForeignKey('user.id'))
