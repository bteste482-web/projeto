from models.db import db
from models.book import Book

def add_book(title, author, description):
    # Check if book already exists
    existing_book = Book.query.filter_by(title=title, author=author).first()
    if existing_book:
        return {"error": "Book already exists"}
    
    # Validate inputs
    if not title or not author or not description:
        return {"error": "Missing required fields"}
    
    try:
        new_book = Book(title=title, author=author, description=description)
        db.session.add(new_book)
        db.session.commit()
        return {"success": "Book created successfully"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def update_book(book_id, title=None, author=None, description=None):
    try:
        book = Book.query.get(book_id)
        if not book:
            return {"error": "Book not found"}
        
        if title:
            existing = Book.query.filter_by(title=title, author=author or book.author).first()
            if existing and existing.id != book_id:
                return {"error": "Book already exists"}
            book.title = title
        
        if author:
            book.author = author
        
        if description:
            book.description = description
        
        db.session.commit()
        return {"success": "Book updated successfully"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def delete_book(book_id):
    try:
        book = Book.query.get(book_id)
        if not book:
            return {"error": "Book not found"}
        
        db.session.delete(book)
        db.session.commit()
        return {"success": "Book deleted successfully"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}
