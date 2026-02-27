# Folder 2: Video - 24 : first class function in python


def greet():
    print("Hello")

hello = greet
hello() # Hello 

# Another example

avg = lambda seq: sum(seq) / len(seq)
total = sum
top = max

operations = {
    "average": avg,
    "total": total,
    "top": top
}

students = [
    {"name": "Rolf", "grades": [70, 88, 90]},
    {"name": "Bob", "grades": [100, 90, 80]},
    {"name": "Jen", "grades": [80, 90, 100]},
    {"name": "Charlie", "grades": [70, 90, 100]}
]

for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"Student: {name}")
    operation = input ("Enter 'average', 'total', or 'top': ")

    operation_function = operations[operation]
    print(operation_function(grades) )

    # if operation == "average": 
    #     print(avg(grades))
    # elif operation == "total":
    #     print(total(grades))
    # elif operation == "top":
    #     print(top(grades))