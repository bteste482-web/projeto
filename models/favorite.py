from models.db import db

class Favorites(db.Model):
    __tablename__ = "favorites"

    id =db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer(), db.Foreignkey("users.id"))
    book_id = db.Column(db.Integer(), db.Foreignkey("books.id"))

    users = db.relationship("Users", backref="favorites")
    books = db.relationship("Books", backref="favorites")