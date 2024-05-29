from models import User
from server.app import Session
from flask import request



session = Session()

def get_current_user():
    user_id = request.headers.get('user_id')
    if user_id:
        user = session.get(User, user_id)
        return user
    return None

def add_new_user(first_name, last_name, username, password):
    if not first_name or not last_name or not username or not password:
        print("First name, last name, username and password are required.")
        return
    
    existing_user = session.query(User).filter_by(username=username).first()

    if existing_user:
        print(f"A user with the username {username} already exists.")
        return

    # Create a new user
    user = User(first_name=first_name, last_name=last_name, username=username)
    user.set_password(password)

    session.add(user)
    session.commit()

    print("User added successfully.")

def update_user_password(user_id, new_password):
    user = session.get(User, user_id)
    if user:
        user.set_password(new_password)
        session.commit()
    else:
        print("User not found.")
