import bcrypt
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///app.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    connections = relationship("Connection", back_populates="user")

    def set_password(self, password):
        # Hash and store the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.password = hashed_password.decode('utf-8')

    def check_password(self, password):
        # Verify the provided password against the stored hash
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    path = Column(String(100), nullable=False)
    connections = relationship("Connection", back_populates="book")


class Connection(Base):
    __tablename__ = 'connections'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    date_added = Column(DateTime, nullable=False)
    page_number = Column(Integer, nullable=False)

    user = relationship("User", back_populates="connections")
    book = relationship("Book", back_populates="connections")


class Quote(Base):
    __tablename__ = 'quotes'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    quote = Column(String(500), nullable=False)

    user = relationship("User", backref="quotes")
    book = relationship("Book", backref="quotes")
