from models.db import db,datetime

class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    email = db.Column(db.String(), nullable=False)
    password_hash = db.Column(db.Integer(), nullable=False)
    created_at = db.Column(db.DateTime ,default=datetime.now())

    favorites = db.relationship("Favorites", backref="userId")
    review = db.relationship("Reviews", backref="bookId")