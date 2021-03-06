from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    c_firstName = db.Column(db.String(150))
    c_email = db.Column(db.String(150), unique=True)
    c_Comm = db.Column(db.Integer)
    c_Con = db.Column(db.Integer)
    c_Tech = db.Column(db.Integer)
    c_Employ = db.Column(db.Integer)
    c_final_score = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))




class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')