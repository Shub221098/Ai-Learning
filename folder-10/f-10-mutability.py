# Folder 10: Video - 1 : Mutability in python

friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
} 

print(id(friends_last_seen)) # different id with below one

friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}

print(id(friends_last_seen)) 

# Their memory address is different

friends_last_seen['Rolf'] = 0

print(id(friends_last_seen))  

my int = 5
print(id(my_int)) # different address

my_int = my_int + 1 # my_int.__add__(self, 1); return cls(self.value + 1)
print(id(my_int)) # different address
my_int += 1 # my_int.__iadd__(self, 1)

# We can't update integar values, so list, tuples, set are mutable, but integer is not.

friends = ['Rolf', 'Jose']
print(id(friends)) # same id

friends.append("Jen")
print(id(friends)) # same id

""" Immutable
integers -> all function returns new int objects
floats
strings
tuples
"""

