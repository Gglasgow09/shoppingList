from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, ShoppingList, Base
from faker import Faker
from random import randint

fake = Faker()

# Set up the database
engine = create_engine('sqlite:///shopping_list.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# User data
user_data = [
    {'username': 'user1', 'password': 'password1'},
    {'username': 'user2', 'password': 'password2'},
]

# Insert Users with hashed passwords
for data in user_data:
    # Check if the user already exists
    existing_user = session.query(User).filter_by(username=data['username']).first()
    if not existing_user:
        user = User(username=data['username'])
        user.set_password(data['password'])
        session.add(user)
session.commit()

# Shopping list data
shopping_list_data = [
    {'item': 'item1', 'quantity': 5, 'user_id': 1},
    {'item': 'item2', 'quantity': 3, 'user_id': 2},
]

# Insert initial shopping list items
for data in shopping_list_data:
    item = ShoppingList(**data)
    session.add(item)
session.commit()

# Add 10 customers using Faker
for _ in range(10):
    user_data = {
        'username': fake.user_name(),
        'password': fake.password()
    }
    # Check if the user already exists
    existing_user = session.query(User).filter_by(username=user_data['username']).first()
    if not existing_user:
        user = User(username=user_data['username'])
        user.set_password(user_data['password'])
        session.add(user)
    session.commit()

# Get all users
users = session.query(User).all()

# For each user, generate a random number of items
for user in users:
    for _ in range(randint(1, 10)):  # Generate 1 to 10 items per user
        shopping_list_data = {
            'item': fake.word(),
            'quantity': randint(1, 10),
            'user_id': user.id,
        }
        item = ShoppingList(**shopping_list_data)
        session.add(item)
session.commit()

print("Database seeded successfully!")
