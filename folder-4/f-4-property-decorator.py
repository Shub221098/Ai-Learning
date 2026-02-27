# Folder 4: Video - 10 : Property Decorators in python

# It is used to access a function as an attribute, so we can access it like an attribute without calling it like a function. It is used to make the code more readable and to avoid calling the function like a method.

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    @property # this will make the weekly_salary method a property, so we can access it like an attribute
    def weekly_salary(self):
        return self.salary * 40

rolf = WorkingStudent("Rolf", "MIT", 15)

print(rolf.weekly_salary) # this will call the weekly_salary method of the WorkingStudent class


# Anothwr example

class Movie:
    def __init__(self, rating):
        self._rating = rating

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not (1 <= value <= 10):
            raise ValueError("Rating must be between 1 and 10")
        self._rating = value


m = Movie(8)
print(m.rating)   # access like an attribute

m.rating = 9      # validation happens
# m.rating = 15 ❌ ValueError