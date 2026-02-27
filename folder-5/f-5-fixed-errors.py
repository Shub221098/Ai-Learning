# Folder 5: Video - 3: Fixed Errors in Python

# IndexError

# Python 3.6.0 (v3.6.0:6c4cf7223x11, Dec 22 2016, 9:12:15)
# [GCC 4.2.1 (Apple Inc. build 5659)] (dot .app) on darwin
# Type "help", "copyright", "credits" or "license" for more information.

# >>> friends = ['Rolf', 'Anne']
# >>> print(friends[5])

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range

# KeyError

# Traceback (most recent call last):
#   File "/Users/jslvtr/Desktop/milestone_1/app.py", line 88, in <module>
#     menu()
#   File "/Users/jslvtr/Desktop/milestone_1/app.py", line 37, in menu
#     show_movies(movies)
#   File "/Users/jslvtr/Desktop/milestone_1/app.py", line 60, in show_movies
#     show_movie_details(movies)
#   File "/Users/jslvtr/Desktop/milestone_1/app.py", line 66, in show_movie_details
#     print(f"release year: {movie['release']}")
# KeyError: 'release'

# def show_movie_details(movie):
#     print(f"Name: {movie['name']}")
#     print(f"Director: {movie['director']}")
#     print(f"Year: {movie['release']}")

# NameError

# Python 3.6.0 (v3.6.0:6c4cf7223x11, Dec 22 2016, 1:12:11)
# [GCC 4.2.1 (Apple Inc. build 5659)] (dot .app) on darwin
# Type "help", "copyright", "credits" or "license" for more information.

# >>> print(hello)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'hello' is not defined


# AttributeError

# Python 3.6.0 (v3.6.0:6d7f92631a11, Dec 22 2016, 11:23:11)
# [GCC 4.2.1 (Apple Inc. build 5659)] (dot .app) on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# friends = ['Rolf', 'Jose', 'Charlie']
# >>> friends_nearby = ['Rolf', 'Anne']
# >>> print(friends_nearby.intersection(friends)) 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'list' object has no attribute 'intersection'


# NotImplementedError

# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

#     def login(self):
#         raise NotImplementedError("This method has not been implemented yet.")


# RunTimeError
# It comes when you are running your program


# SyntaxError

# class User (Colon is missing)
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

# IndentationError

# def add_two(x, y):
# return x + y

# TabError

# def add_two(x, y):
# __return x + y

# def pow(n, exp):
#   return n**exp


# TypeError

# Python 3.6.0 (v3.6.0:6d7f92631a11, Dec 22 2016, 1:12:11)
# [GCC 4.2.1 (Apple Inc. build 5659)] (dot .app) on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> 5 + 5
# 10
# >>> 'hi' + 'ha'
# 'hiha'
# >>> 5 + 'hi'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'int' and 'str'


# ValueError

# Python 3.6.0 (v3.6.0:6d7f92631a11, Dec 22 2016, 1:23:13)
# [GCC 4.2.1 (Apple Inc. build 5659)] (dot .app) on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> int('20.5')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '20.5'


# ImportError

# from math import squareroot
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ImportError: cannot import name 'squareroot' from 'math' (unknown location)


# DeprecationWarning

# from database import Database
#
# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#
#     def register(self):
#         Database.write(self.username, self.password)
#         raise DeprecationWarning('UserException still works, but is deprecated.')
#
#     @classmethod
#     def register_user(cls, username, password):
#         Database.write(username, password)
#         return cls(username, password)

