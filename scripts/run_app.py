from services import user_session
from services import database_setup
from services.app import engine


def main():
    # start GUI
    # when the user logs in, we get his name:
    # using the name we can get an id. Let's assume it's 1
    user_id = 1
    session = user_session.Session(engine, user_id)

    # after logging in the user performs actions
    # 1. opens settings: nothing to be implemented using backend
    # 2. opens all books:
    #   - gets a list of all books: TODO: get all books from the database with markers added or not
    #   - removes and adds books: in user_session.py
    #   - can get a description of a book() TODO: get a description of a book
    # 3. opens added_books:
    #   - gets a list of all his books: session.get_user_books()
    #   - removes and adds books: session.remove_connection() and session.add_connection()
    #   - opens a book in added_books. book_session.py
    # 4. opens his favourite citations:
    #   - gets a list of all his favourite citations: user_session.get_user_quotes()
    # 5. the user logs out: session.__exit__()
    # we return to the start of the program
