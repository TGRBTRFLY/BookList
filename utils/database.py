import sqlite3

"""
Concerned wit storing an retrieving books from a database.
"""


def create_book_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS books(title text, author text, read integer)')

    connection.commit()
    connection.close()


def add_book(title, author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (title, author))

    connection.commit()
    connection.close()


def get_all_books():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books')
    books = [{'title': row[0], 'author': row[1], cursor.fetchall()

        connection.close()


def mark_book_as_read(title):
    for book in books:
        if book['title'] == title:
            book['read'] = True


def delete_book(title):
    global books
    books = [book for book in books if book['title'] != title]  # add each book to new list
