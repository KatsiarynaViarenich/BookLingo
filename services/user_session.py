from services.database_setup import Book, Connection, Quote, User


class Session:
    def __init__(self, engine, user_id):
        self.engine = engine
        self.session = None
        self.user_id = user_id

    def __enter__(self):
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        return self.session

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.session.close()
        self.session = None
        self.user_id = None
        return False

    def add_connection(self, book_id):
        user = self.session.query(User).get(self.user_id)
        book = self.session.query(Book).get(book_id)

        if user is None:
            print(f"User with ID {self.user_id} does not exist.")
            return

        if book is None:
            print(f"Book with ID {book_id} does not exist.")
            return

        connection = Connection(user=user, book=book)
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

    def get_connections(self):
        return self.session.query(Connection).all()

    def get_user_connections(self):
        return self.session.query(Connection).filter_by(user_id=self.user_id).all()

    def get_user_books(self):
        return self.session.query(Book).join(Connection).filter(Connection.user_id == self.user_id).all()

    def get_user_quotes(self):
        return self.session.query(Quote).filter_by(user_id=self.user_id).all()