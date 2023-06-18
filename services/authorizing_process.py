from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import bcrypt
from database_setup import Base

engine = create_engine('sqlite:///app.db')
Session = sessionmaker(bind=engine)
session = Session()


def create_new_account(username, password):
    if session.query(User).filter_by(username=username).first():
        return "Username already exists"

    new_user = User(username=username)
    new_user.set_password(password)

    session.add(new_user)
    session.commit()

    return "Account created successfully"


def log_in(username, password):
    user = session.query(User).filter_by(username=username).first()

    if user and user.check_password(password):
        return "Login successful"
    else:
        return "Invalid username or password"