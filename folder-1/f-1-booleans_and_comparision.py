# Folder 1: Video - 14 : Booleans and Comparisions

truthy = True
falsy = False

age = 20
is_over_age = age >= 18 # boolean comparision
is_under_age = age <= 18  # false
is_twenty = age == 20 # true

# one equal is for assignment, two equal sign is for checking

# Let's create a simple program that will ask the user for number and will check whether it matches or magic number

my_number = 5
user_number = int(input("Enter your number: "))

print(my_number == user_number)

matches = my_number == user_number
print(f"You got it right: {matches}.")