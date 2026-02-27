# Folder 2: Video - 23 : lambda function in python

def divide(x, y):
    return x / y

divide = lambda x, y: x / y

# Call lambda funciton ways

print(divide(10, 2)) # 5.0
divide = lambda x, y: x / y
print(divide(10, 0)) # Cannot divide by zero

print((lambda x, y: x / y)(10, 0))


def average(sequence):
    return sum(sequence) / len(sequence)

average = lambda sequence: sum(sequence) / len(sequence)

students = [
    {"name": "Rolf", "grades": [70, 88, 90]},
    {"name": "Bob", "grades": [100, 90, 80]},
    {"name": "Jen", "grades": [80, 90, 100]},
    {"name": "Charlie", "grades": [70, 90, 100]}
]

for student in students:
    print(average(student["grades"]))