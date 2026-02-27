# Folder 4: Video - 3 : classes and objects Python
class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student_one = Student("Rolf Smith", [78,45,48, 23])
student_two = Student("Jose", [34, 45, 98, 38])

# Folder 4: Video - 6 : parameter naming in Python

class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year

movie_one = Movie("The Matrix", 1999)
print(movie_one.name)

# Use parameter names to make it more clear