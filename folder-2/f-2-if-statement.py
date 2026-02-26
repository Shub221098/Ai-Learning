friend = "Rolf"
user_name = input("Enter your name: ")

if user_name == friend:
    print("Hello, friend!") # add 4 spaces in front
    print("This runs too.")
else:
    print("This runs anyway.") # it is outside of if statement always runs.

# in lists check using in
friends = ["Rolf", "Bob", "Anne"]
family = ["Jen", "Charlie"]

user_name = input("Enter your name: ")

if user_name in friends:
    print("Hello, friend!")
elif user_name in family:
    print("Hello, Family!")
else:
    print("I don't know you")