# Folder 2: Video - 2 : WHILE LOOPS

# is_learning = True

# while is_learning:
#     print("You are learning")
#     user_input = input("Are you still learning?")
#     is_learning = user_input == "yes"


# user_input = input("Do you wish to run the program (yes/no): ")

# while user_input == "yes":
#     print("We are running!")
#     user_input = input("Do you wish to run the program? (yes/no): ")

# print("We stopped running")



# Folder 2: Video - 4 : FOR LOOPS

friends = ["Rolf", "Jen", "Anne"]
for friend in friends:
    print(friend)

elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for index in elements:
    print(index)
    print("Hello, world!") # here as we are not using index so we can write for _ in elements

for index in range(10):
    print(index)

for index in range(5, 10):
    print(index) # 5 6 7 8 9


for index in range(2, 20, 3):
    print(index) # 2 5 8 11 14 17


students = [
    {"name": "Rolf", "grade" :90 },
    {"name": "Bob", "grade" :78 },
    {"name": "Jen", "grade" :100 },
    {"name": "Anne", "grade" :80 }
]

for student in students:
    name = student["name"]
    grade = student["grade"]

    print(f"{name} has a grade of {grade}.")