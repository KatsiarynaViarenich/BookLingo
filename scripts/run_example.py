from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from services import user_session
from services.database_setup import User, Book
from services.user_session import UserSession


def main():
    # here is a flow of the program
    engine = create_engine('sqlite:///app.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    user1 = User(name='John', password='password1')
    user2 = User(name='Alice', password='password2')
    session.add(user1)
    session.add(user2)

    book1 = Book(title='Book 1', author='Author 1', path="../data/The_Little_Mermaid-Hans_Andersen.epub",
                 description='Description 1')
    book2 = Book(title='Book 2', author='Author 2', path="../data/The_Little_Mermaid-Hans_Andersen.epub",
                 description='Description 2')
    session.add(book1)
    session.add(book2)

    # start GUI
    # when the user logs in, we get his name.
    user_id = session.query(User).filter_by(name='John').first().id
    print(user_id)
    user_session = UserSession(session, user_id)

    # 1. opens settings: nothing to be implemented using backend

    # 2. opens all books:
    #   - gets a list of all books: TODO: get all books from the database with markers added or not
    #   - removes and adds books: session.remove_connection() and session.add_connection()
    #   - gets a description of a book() TODO: get a description of a book

    # 3. opens his books:
    #   - gets a list of all his books: session.get_user_books()
    #   - removes and adds books: session.remove_connection() and session.add_connection()
    #   - opens a book in added_books: book_session.py. here he can scroll pages, add a quote, use the modules

    user_session.add_connection(book1.id)
    book_session = user_session.open_book(book1.id)
    for book in user_session.get_user_books():
        print(book)
        print()

    for page in book_session.book_pages:
        print(page)
        print()

    # for book in user_session.get_all_books():
    #     print(book)
    #     print()

    user_session.remove_connection(book1.id)

    book_session.add_quote("This is a quote")

    print(user_session.get_user_quotes())


main()