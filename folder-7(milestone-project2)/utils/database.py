"""
Concerned with storing and retrieving books form a list.
"""

books = [] # this is our in-memory database

def add_book(name, author):
    book = {
        "name": name,
        "author": author,
        "read": False
    }
    books.append(book)

def get_all_books():
    return books

def mark_book_as_read(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True
            break

def delete_book(name):
    global books
    books = [book for book in books if book['name'] != name ]
    
# def delete_book(name):
#     for book in books:
#         if book['name'] == name:
#             books.remove(book)
#             break

