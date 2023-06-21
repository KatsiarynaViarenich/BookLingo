from asyncio import sleep
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from run_setup import User, Book, Connection
from services.user_session import UserSession
from services.authorizing_process import AuthorizingProcess


def main():
    # here is a flow of the program
    engine = create_engine('sqlite:///../data/app.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    authorizing_process = AuthorizingProcess(session)
    authorizing_process.create_new_account('John', 'password1')
    authorizing_process.create_new_account('Alice', 'password2')
    print('Accounts created')
    print()

    if authorizing_process.log_in('John', 'password1') == 'Login successful':
        print('John logged in')
        user_session = UserSession(session, session.query(User).filter_by(name='John').first().id)
    else:
        return
    print()

    print('John added some books:')
    user_session.add_connection(book_id=3)
    user_session.add_connection(book_id=5)
    user_session.add_connection(book_id=1)
    print()

    # below all the sorting methods go
    books = user_session.get_user_books(sort_by=Book.title)
    books = user_session.get_user_books(sort_by=Book.title.desc())
    books = user_session.get_user_books(sort_by=Book.author)
    books = user_session.get_user_books(sort_by=Book.author.desc())
    books = user_session.get_user_books(sort_by=Connection.date_added)
    books = user_session.get_user_books(sort_by=Connection.date_added.desc())

    print("Here are the Johns books:")
    for book in books:
        print(book.title)
    print()

    # filtering by a title:
    print("Here are the Johns books (filtered):")
    books = user_session.get_user_books(sort_by=Book.title, filter_by='Alice')
    for book in books:
        print(book.title)
    print()

    print("Here are the books that John possibly wants to add:")
    for book in user_session.get_other_books():
        print(book.title)
    print()

    print("John opened a book:")
    book_session = user_session.open_book(1)
    for page in book_session.book_pages:
        print(page)
        print()

    print("John adds quotes:")
    book_session.add_quote("This is a quote")

    book_session = user_session.open_book(3)

    book_session.add_quote("This is a second quote")
    book_session.add_quote("This is a third quote")
    print()

    print("Here are the quotes:")
    for title, author, quote in user_session.get_user_quotes():
        print(quote + " - " + title + " by " + author)


main()
