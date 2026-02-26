# Folder 1: Video - 15 : and & or in python

age = 25

result = age > 18 and age < 30 # True and True
print(result)

result = age < 18 and age < 30 # False and True


age = 25

result = age > 18 or age < 65 # False or True
print(result)

# Truthy Falsy value testing

bool(0) # False, zero
bool(13) # True

bool("") # False, empty string
bool("Hello") # True

bool([])  # False, empty list
bool([1, 3, 5]) # True

# Example: 1
default_age = 30
age = 0

user_age = age or default_age
print(user_age) # 30

# Example: 2
default_greeting = "There"
name = input("Enter you anem : {optional}")

user_name = name or default_greeting
print(f"Hello, {user_name}!")
