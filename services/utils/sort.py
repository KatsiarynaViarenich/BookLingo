def sort_books_by_author(books):
    return sorted(books, key=lambda book: book.author)


def sort_books_by_title(books):
    return sorted(books, key=lambda book: book.title)


def sort_books_by_date_added(books):
    return sorted(books, key=lambda book: book.date_added)


def sort_quotes_by_date_added(quotes):
    return sorted(quotes, key=lambda quote: quote.date_added)


def sort_quotes_by_book(quotes):
    return sorted(quotes, key=lambda quote: quote.book.title)
