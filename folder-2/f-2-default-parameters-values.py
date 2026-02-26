# Folder 2: Video - 22 : default parameter values in python

def add(x, y=3):
    total = x + y
    return total

print(add(5, 6))

print(add(x=5, y=2))
print(add(y=2)) # throw error x is required argument

print(1, 2, 3, 4, 5, sep=" - ") # built in function 1 - 2 - 3 - 4 - 5

 