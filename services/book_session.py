import re

import ebooklib
from bs4 import BeautifulSoup
from ebooklib import epub

from services.database_setup import Book, Connection, Quote, User


def split_book_into_pages(book_path, characters_per_page=1500):
    book = epub.read_epub(book_path)
    pages = []
    page_content = ""

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            content = item.get_content()
            soup = BeautifulSoup(content, "html.parser")
            clean_text = soup.get_text(separator=" ")
            clean_text = re.sub('\n{2,}', '\n', clean_text)
            clean_text = clean_text.rstrip('\n')
            words = clean_text.split()

            for word in words:
                if len(page_content) + len(word) + 1 <= characters_per_page:
                    page_content += word + " "
                else:
                    pages.append(page_content.strip())
                    page_content = word + " "

            if page_content:
                pages.append(page_content.strip())
    return pages


class BookSession:
    def __init__(self, session, book_id, user_id, page_number=0):
        self.session = session
        self.book_id = book_id
        self.user_id = user_id
        self.book_path = self.session.query(Book).get(self.book_id).path
        self.book_pages = split_book_into_pages(self.book_path)
        self.page_number = page_number

    def add_quote(self, quote):
        book = self.session.query(Book).get(self.book_id)
        user = self.session.query(User).get(self.user_id)

        if book is None:
            print(f"Book with ID {self.book_id} does not exist.")
            return

        if user is None:
            print(f"User with ID {self.user_id} does not exist.")
            return

        quote = Quote(user=user, book=book, quote=quote)
        self.session.add(quote)
        self.session.commit()
        print(f"Quote added: User {user.name} <-> Book {book.title}")

    def update_page_number(self, page_number):
        connection = (
            self.session.query(Connection)
            .filter(Connection.user_id == self.user_id)
            .filter(Connection.book_id == self.book_id)
            .first()
        )
        connection.page_number = page_number
        self.session.commit()
        print(f"Page number updated: {page_number}")
