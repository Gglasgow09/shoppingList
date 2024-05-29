from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, ShoppingListItem, Base
from faker import Faker


fake = Faker()
engine = create_engine('sqlite:///shopping-list.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


user_data = [
    {'user_name: ', 'password: '}
]

item_data = [
    {'name: ', 'quantity: ' }
]

#Insert Users
for data in user_data:
    user= User(**data)
    session.add(user)
session.commit()

#Insert Items
for data in item_data:
    item = ShoppingListItem(**data)
    session.add(ShoppingListItem)
session.commit()
    
# Add 10 customers using faker
highest_id = session.query(User).order_by(User.id.desc()).first().id

for _ in range(10):
    highest_id += 1
    customer_data = {
        'user_name': fake.user_name(),
        'password': fake.password(),
    }
    user = User(**user_data)
    session.add(user)
    session.commit()  

