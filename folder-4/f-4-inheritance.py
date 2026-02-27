# Folder 4: Video - 9 : Inheritance in python

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        # self.name = name
        # self.school = school
        # self.marks = []
        super().__init__(name, school) # inheritance : this will call the __init__ method of the Student class
        self.salary = salary

    def weekly_salary(self):
        return self.salary * 40

rolf = WorkingStudent("Rolf", "MIT", 15)
print(rolf.name)
print(rolf.salary)
rolf.marks.append(80)
rolf.marks.append(90)

print(rolf.average())

anna = Student("Anna", "Harvard")
print(anna.school) # This is valid since Anna is a Student object
# print(anna.salary) # error - Anna doesn't have a salary attribute
# anna.weekly_salary() # error - Anna doesn't have a weekly_salary method