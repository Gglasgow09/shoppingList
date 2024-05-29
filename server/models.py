import re
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, validates, declarative_base
import bcrypt

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String, unique=True)
    shopping_lists = relationship('ShoppingList', back_populates='user')

    @validates('username')
    def validate_username(self, key, username):
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            raise ValueError('Invalid username')
        return username
 
    @validates('password')
    def validate_password(self, key, password):
        if len(password) < 8:
            raise ValueError('Password is too short')
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def set_password(self, password):
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
    

class ShoppingList(Base):
    __tablename__ = 'shopping_lists'
    id = Column(Integer, primary_key=True)
    item = Column(String)
    quantity = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='shopping_lists')
    

