import tkinter as tk
import ebooklib
from bs4 import BeautifulSoup
from ebooklib import epub


class BookSession:
    def __init__(self, book_title, book_path):
        self.book_title = book_title
        self.pages = self.split_book_into_pages(book_path)
        self.current_page = 0

    def split_book_into_pages(self, book_path, characters_per_page=1000):
        book = epub.read_epub(book_path)
        pages = []

        for item in book.get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                content = item.get_content()
                soup = BeautifulSoup(content, 'html.parser')
                clean_text = soup.get_text(separator=' ')

                page_count = len(clean_text) // characters_per_page + 1
                for i in range(page_count):
                    start = i * characters_per_page
                    end = (i + 1) * characters_per_page
                    page_content = clean_text[start:end]
                    pages.append(page_content)

        return pages