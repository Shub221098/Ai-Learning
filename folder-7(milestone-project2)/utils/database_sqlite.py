from .database.connection import DatabaseConnection
"""
Concerned with storing and retrieving books form a sqlite database.
Format of the database:
name | author | read
"""

def create_books_table():
    with DatabaseConnection('data.db') as connection:
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS books (name TEXT, author TEXT, read INTEGER)')
    # connection = sqlite3.connect('data.db')
    # cursor = connection.cursor()
    # cursor.execute('CREATE TABLE IF NOT EXISTS books (name TEXT, author TEXT, read INTEGER)')
    # connection.commit()
    # connection.close()

    # with sqlite3.connect('data.db') as connection:
    #     cursor = connection.cursor()
    #     cursor.execute('CREATE TABLE IF NOT EXISTS books (name TEXT, author TEXT, read INTEGER)')
    #     connection.commit()
    #     connection.close()

def add_book(name, author):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books VALUES (?, ?, ?)', (name, author, 0))

    # connection = sqlite3.connect('data.db')
    # cursor = connection.cursor()
    # # cursor.execute(f'INSERT INTO books VALUES ("{name}", "{author}", 0)')
    # cursor.execute('INSERT INTO books VALUES (?, ?, ?)', (name, author, 0))
    # connection.commit()
    # connection.close()

def get_all_books():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books')
        books = [
            {"name": row[0], "author": row[1], "read": bool(row[2])}
            for row in cursor.fetchall()
        ]
        return books

    # connection = sqlite3.connect('data.db')
    # cursor = connection.cursor()
    # cursor.execute('SELECT * FROM books')
    # books = [
    #     {"name": row[0], "author": row[1], "read": bool(row[2])}
    #     for row in cursor.fetchall()
    # ]
    # connection.close()
    # return books

def mark_book_as_read(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read = 1 WHERE name = ?', (name,))

    # connection = sqlite3.connect('data.db')
    # cursor = connection.cursor()
    # cursor.execute('UPDATE books SET read = 1 WHERE name = ?', (name,))
    # connection.commit()
    # connection.close()

def delete_book(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE name = ?', (name,))
    # connection = sqlite3.connect('data.db')
    # cursor = connection.cursor()
    # cursor.execute('DELETE FROM books WHERE name = ?', (name,))
    # connection.commit()
    # connection.close()