from db import db,datetime

class Reviews(db.Model):
    __tablename__ = 'review'

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.Foreignkey("users.id"))
    book_id =  db.Column(db.Integer(), db.Foreignkey("books.id"))
    rating = db.Column(db.Integer(), nullable=False)
    comment =  db.Column(db.String(100), nullable=True)
    created_at =  db.Column(db.Datetime, default=datetime.now())

    users = db.relationship("Users", backref="reviews")
    books = db.relationship("Books", backref="reviews")