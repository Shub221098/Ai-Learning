# Folder 4: Video - 1 : Intro to OOPS in Python
# OOPS stands for Object Oriented Programming System
# OOPS is a programming paradigm that uses objects and classes to structure code
# OOPS allows us to model real-world entities as objects in our code, making it easier


my_student = {
    "name": "Ankit",
    "age": 25,
    "grades": [90, 85, 92, 100],
    "average": average_grade(my_student)
}

def average_grade(student):
    return sum(student["grades"]) / len(student["grades"])
    print(average_grade(my_student))

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades) 

my_student = Student("Ankit", 25, [90, 85, 92, 100])
print(my_student.name)
print(my_student.average())