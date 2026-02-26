# Folder 2: Video - 12 : list-slicing in python

friends = ["Rolf", "Charlie", "Anna", "Bob", "Jen"]

# Get elements from index 2, 3 
print(friends[2:4]) # ["Anna", "Bob" ]
# Get elements except the first one.
print(friends[1:]) # ["Charlie", "Anna", "Bob", "Jen" ]
# Get elements excepts the 4th one.
print(friends[:4]) # ["Rolf", "Charlie", "Anna", "Bob" ]

# Get new list which contains all of the elements of old list
print(friends[:]) # ["Rolf", "Charlie", "Anna", "Bob", "Jen"]

print(friends[-3:4]) # ["Anna", "Bob" ]

print(friends[:-2]) # ["Rolf", "Charlie", "Anna" ]

print(friends[-3:-1]) # ["Anna", "Bob" ]