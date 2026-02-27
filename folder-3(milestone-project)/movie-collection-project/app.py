# Add new movies to my collection to keep track
# List all the movies I have in my colleciton
# Find a movie by using a movie title


# Planning
# Where is the data of movies store in code
# What data we want to store for each movie
# Show the user a menu and let them pick an option
# Implement each requirement in turn, each as a sepearte function
# Stop running the program when they type 'q' in the menu


# Where data store of movies
# We'll use a list of dictionaries to store the movies
# Each dictionary will represent a movie with keys like "title", "director", and "year"

MENU_PROMPT="\nEnter 'a' to add a movie, 'l' to list movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []

def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        "title": title,
        "director": director,
        "year": year
    })

def show_movies():
    for movie in movies:
        print(f"{movie['title']} ({movie['year']}), directed by {movie['director']}")

def print_movie(movie):
    print(f"{movie['title']} ({movie['year']}), directed by {movie['director']}")

def find_movie():
    search_title = input("Enter the movie title to search for: ")
    for movie in movies:
        if movie['title'].lower() == search_title.lower():
            print(f"Found: {movie['title']} ({movie['year']}), directed by {movie['director']}")
            break
    else:
        print("Movie not found.")

def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'a':
            add_movie()
        elif selection == 'l':
            show_movies()
        elif selection == 'f':
            find_movie()
        else:
            print("Invalid option, please try again.")

        selection = input(MENU_PROMPT)

# first class functions
user_options = {
    "a": add_movie,
    "l": show_movies,
    "f": find_movie,
}

selection = input(MENU_PROMPT)
while selection != 'q':
    if selection in user_options:
        selected_function = user_options[selection]
        selected_function()
    else:
        print("Invalid option, please try again.")

    selection = input(MENU_PROMPT)

menu()
