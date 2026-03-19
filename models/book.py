from db import db,datetime

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    title = db.Column(db.String(), nullable=False)
    author = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime , default=datetime.now())

    favorites = db.relationship("Favorites", backref="userId")
    review = db.relationship("Reviews", backref="bookId")