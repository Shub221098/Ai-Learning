# Folder 9: Video - 8 : Any & all in python


friends = [
    {
        'name': "Rolf",
        'location': "Washigton, D.C."
    },
    {
        'name': "Anna",
        'location': "Washigton, D.C."
    },
    {
        'name': "Charlie",
        'location': "San Francisco"
    },
    {
        'name': "Jose",
        'location': "San Francisco"
    },
]

your_location = input("Where are you right now? ")
friends_nearby = [friend for friend in friends if friend['location' == your_location]]

if any(friends_nearby):
    print("You are not alone!")

print(all([0, 1, 2, 3, 4, 5]))

"""
* 0, 0.0
* None
* [] () {}
* False
"""

print(bool(0)) # false