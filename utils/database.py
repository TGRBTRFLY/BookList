from .database_connection import DatabaseConnection

"""
Concerned wit storing an retrieving books from a database.
"""


def create_book_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS books(title text, author text, read integer)')


def add_book(title, author):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (title, author))


def get_all_books():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')
        books = [{'title': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]

    return books


def mark_book_as_read(title):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE books SET read=1 WHERE title=?', (title,))


def delete_book(title):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM books WHERE title=?', (title,))


"""

















"""
