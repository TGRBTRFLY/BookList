import json

"""
Concerned wit storing an retrieving books from a database.
"""

books_file = 'books.json'

books = []


def create_book_table():
    with open(books_file, 'w') as file:
        json.dump([], file)


def add_book(title, author):
    books = get_all_books()
    books.append({'title': title, 'author': author, 'read': False})
    _save_all_books(books)


def get_all_books():
    with open(books_file, 'r') as file:
        return json.load(file)


def mark_book_as_read(title):
    for book in books:
        if book['title'] == title:
            book['read'] = True


def delete_book(title):
    global books
    books = [book for book in books if book['title'] != name]  # add each book to new list


def save_all_books(books):
    with open(books file, 'w') as file:
