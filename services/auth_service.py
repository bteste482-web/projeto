from models.db import db
from models.user import Users
from werkzeug.security import generate_password_hash

def add_auth(username, email, password):
    # Check if user already exists
    existing_user = Users.query.filter_by(username=username).first()
    if existing_user:
        return {"error": "Username already exists"}
    
    existing_email = Users.query.filter_by(email=email).first()
    if existing_email:
        return {"error": "Email already exists"}
    
    # Validate inputs
    if not username or not email or not password:
        return {"error": "Missing required fields"}
    # Validar comprimento mínimo de senha
    if len(password) < 6:
        return {"erro": "A senha deve ter pelo menos 6 caracteres"}
    try:
        new_user = Users(username=username, email=email, password_hash=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        return {"success": "User created successfully"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def update_auth(user_id, username=None, email=None, password=None):
    try:
        user = Users.query.get(user_id)
        if not user:
            return {"error": "User not found"}
        
        if username:
            existing = Users.query.filter_by(username=username).first()
            if existing and existing.id != user_id:
                return {"error": "Username already exists"}
            user.username = username
        
        if email:
            existing = Users.query.filter_by(email=email).first()
            if existing and existing.id != user_id:
                return {"error": "Email already exists"}
            user.email = email
        
        if password:
            user.password_hash = generate_password_hash(password)
        
        db.session.commit()
        return {"success": "User updated successfully"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def delete_auth(user_id):
    try:
        user = Users.query.get(user_id)
        if not user:
            return {"error": "User not found"}
        
        db.session.delete(user)
        db.session.commit()
        return {"success": "User deleted successfully"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

user = Users.query.all()
