import re
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table, Index
from sqlalchemy.orm import relationship, validates, declarative_base
import bcrypt

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
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

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
    
class ShoppingList(Base):
    __tablename__ = 'shopping_lists'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='shopping_lists')
    items = relationship('Item', back_populates='shopping_list')