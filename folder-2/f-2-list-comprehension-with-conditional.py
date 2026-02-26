# Folder 2: Video - 13 : list-comprehension with conditionals in python

# Filter out some elements while putting into new lists

ages = [27, 35, 27, 21, 20]
odds = [age for age in ages if age % 2 == 1]
print(odds) # [35, 27, 21]

friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

# One way to do it
friends_lower = set([f.lower() for f in friends])
guests_lower = set([g.lower() for g in guests])

print(friends_lower.intersection(guests_lower))


# Another way using list comprehension
friends_lower = [f.lower() for f in friends]
present_friends = [
    name.title()
    for name in guests
    if name.lower() in friends_lower
]
print(present_friends)  

# Not good
friends_lower = [f.lower() for f in friends]
present_friends = [
    name for name in guests if name.lower() in [f.lower() for f in friends]
]
print(present_friends)  