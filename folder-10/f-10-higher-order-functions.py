# Folder 10: Video - 18 : Higher order functions in python

def greet():
    print("Hello")'
    

def before_and_after(func):
    print("Before...")
    func() # higher order funciton
    print("After...")

# before_and_after(5) # throw error
before_and_after(lambda: 5) # will get before and after log
before_and_after(greet()) # getting error as it pass None to func
before_and_after(greet) # before  hello after will comes

movies = [
    {"name": "The Matrix", "director": "Wachowski"},
    {"name": "A Beutiful Day in the NEighborhood", "director": "Heller"},
    {"name": "The Irishman", "director": "Scorsese"},
    {"name": "Klaus", "director": "Pablos"},
    {"name": "1917", "director": "Mendes"},
]

def find_movie(expected, finder):
    found = []
    for movie in movies:
        if finder(movie) == expected:
            found.append(movie)

find_by = input("What property are we searching by? ")
looking_for = input("What are you looking for? ")
find_movie(looking_for, lambda movie: movie[find_by])

print(movies or 'No movies found.')