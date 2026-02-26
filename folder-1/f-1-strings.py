# Folder 1: Video - 10 : PYthon strings
my_string = "Hello, world!"
print(my_string)
print("Hello, world!")

# if single quotation marks is inside the string then outside string shoudl be double quoted.
string_with_quotes = "Hello, it's me."
another_with_quotes = 'He said "You are amazing!" yesterday.'
# We directly don't use same string quotes inside and outside.
# another_with_quotes = "He said "You are amazing!" yesterday."

# To write same quotes you need to add backslash
another_with_quotes = "He said \"You are amazing!\" yesterday."

 # Multiline strings

multiline = """Hello, world.

My name is Jose. Welcome to my program.
"""
print(multiline)

# Comments using multiline
"""
Strings

This file talks about strings.
"""

name = "Jose"
greeting = "Hello, " + name
print(greeting) # Hello, Jose

age = 34
#print("You are " + age) # In python you will get because you need to convert integer to string first.

age_as_str = str(age)
print("You are " + age_as_str) # You are 34

# Folder 1: Video - 11 : PYthon string formatting

# Instead of doing age_as_str = str(age)
print(f"You are {age}")

name = "Jose"
greeting = f"How are you, {name}?"
print(greeting) # How are you, Jose

name = "Bob" 
print(greeting) # How are you, Jose -- Here name is not changed

# Another format to write

name = "Jose"
final_greeting = "How are you {}?"
jose_greeting = final_greeting.format(name)
print(jose_greeting)

name = "Bob"
bob_greeting = final_greeting.format(name)
print(bob_greeting)

# Another way to write
friend_name = "Jose"
final_greeting = "How are you, {name}?"
jose_greeting = final_greeting.format(name=friend_name) # here name refer to name in final_greeting string and Jose is refer to the variable name
print(jose_greeting)