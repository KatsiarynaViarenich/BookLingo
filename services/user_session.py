from datetime import datetime

from services.book_session import BookSession
from services.database_setup import Book, Connection, Quote, User


class UserSession:
    def __init__(self, session, user_id):
        self.session = session
        self.user_id = user_id

    def add_connection(self, book_id):
        user = self.session.query(User).get(self.user_id)
        book = self.session.query(Book).get(book_id)

        if user is None:
            print(f"User with ID {self.user_id} does not exist.")
            return

        if book is None:
            print(f"Book with ID {book_id} does not exist.")
            return

        connection = Connection(user=user, book=book, date_added=datetime.now(), page_number=0)
        print(datetime.now())
        self.session.add(connection)
        self.session.commit()
        print(f"Connection added: User {user.name} <-> Book {book.title}")

    def remove_connection(self, connection_id):
        connection = self.session.query(Connection).get(connection_id)

        if connection is None:
            print(f"Connection with ID {connection_id} does not exist.")
            return

        self.session.delete(connection)
        self.session.commit()
        print("Connection removed.")


    def open_book(self, book_id):
        book = self.session.query(Book).get(book_id)
        if book is None:
            print(f"Book with ID {book_id} does not exist.")
            return
        page_number = self.session.query(Connection).filter(Connection.user_id == self.user_id).filter(Connection.book_id == book_id).first().page_number
        print(f"Opening book: {book.title}")
        return BookSession(self.session, book_id, self.user_id, page_number)

    def get_user_books(self, sort_by=Book.title, filter_by=None):
        books = self.session.query(Book).join(Connection).filter(Connection.user_id == self.user_id).order_by(sort_by).all()
        if filter_by is not None:
            books = [book for book in books if filter_by in book.title]
        return books

    def get_other_books(self, sort_by=Book.title, filter_by=None):
        books = self.get_user_books()
        other_books = self.session.query(Book).filter(~Book.id.in_([book.id for book in books])).order_by(sort_by).all()
        if filter_by is not None:
            other_books = [book for book in books if filter_by in book.title]
        return other_books

    def get_user_quotes(self):
        quotes = self.session.query(Quote).filter_by(user_id=self.user_id).all()
        quotes_info = []
        for quote in quotes:
            quotes_info.append(self.get_quote_info(quote.id))
        return quotes_info

    def get_quote_info(self, quote_id):
        quote = self.session.query(Quote).get(quote_id)
        book = self.session.query(Book).get(quote.book_id)
        return book.title, book.author, quote.quote

    def remove_quotes(self, quote_id):
        quote = self.session.query(Quote).get(quote_id)

        if quote is None:
            print(f"Quote with ID {quote_id} does not exist.")
            return

        self.session.delete(quote)
        self.session.commit()
        print("Quote removed.")