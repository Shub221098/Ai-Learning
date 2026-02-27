# Folder 5: Video - 2: Introduction to Errors in Python

print(my_variable) # this will raise a NameError since my_variable is not defined

# Example traceback from an error (copied from an image):
# Traceback (most recent call last):
#   File "/Users/jsvtr/Dropbox/teclado/courses/complete-python-course/section3/milestone_1/app.py", line 53, in <module>
#     menu()
#   File "/Users/jsvtr/Dropbox/teclado/courses/complete-python-course/section3/milestone_1/app.py", line 10, in menu
#     show_movies()
#   File "/Users/jsvtr/Dropbox/teclado/courses/complete-python-course/section3/milestone_1/app.py", line 36, in show_movies
#     show_movie_details(movie)
#   File "/Users/jsvtr/Dropbox/teclado/courses/complete-python-course/section3/milestone_1/app.py", line 48, in show_movie_details
#     print(movie['name'])
# TypeError: list indices must be integers or slices, not str

1. At the very bottom it gives you the error that was raised and the type of error that was raised (in this case it is a TypeError).
2. What line of your code raised the error (in this case it is line 48 in the app.py file).
3. The traceback shows you the sequence of function calls that led to the error (in this case it shows that the menu function called the show_movies function, which called the show_movie_details function, which is where the error was raised).
4. What function that line is in;
5. What function called the function that the line is in;
6. And so on... until you reach the file that you expected.

# This is the code of the above error message
def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        "title": title,
        "director": director,
        "year": year
    })

def show_movies(movies_list):
    for movie in movies_list:
        print(f"{movie['title']} ({movie['year']}), directed by {movie['director']}")

def show_movie_details(movie):
    print(f"Name: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")