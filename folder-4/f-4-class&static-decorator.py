# Folder 4: Video - 11 & 12: @classmethod, @staticmethod in Python

# Use class method instead of static methods much.

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

rolf = Student("Rolf", "MIT")
rolf.marks.append(80)
rolf.marks.append(90)
print(rolf.average())

Student.average("hello") # this will give an error since we are trying to call the average method on the Student class, but it is an instance method and it requires an instance of the Student class to be called

class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)

my_object = Foo()
my_object.hi() # this will call the hi method of the Foo class and it will print the name of the class which is Foo

class Bar:
    @staticmethod
    def hi():
        print("Hi there!")

another_object = Bar()
another_object.hi() # this will call the hi method of the Bar class and it will print "Hi there!"


# Advanced example of classmethod and staticmethod

class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"<FixedFloat {self.amount:.2f}>"

    # def from_sum(self, a, b):
    #     return FixedFloat(a + b)

# print(FixedFloat(5.678)) # this will call the __repr__ method of the FixedFloat class and it will print <FixedFloat 5.68>
# number = FixedFloat(5.678)
# print(number.from_sum(1.234, 2.345)) # this will call the from_sum method of the FixedFloat class and it will print <FixedFloat 3.58> since it will add 1.234 and 2.345 and then it will create a new FixedFloat object with the amount of 3.5799999999999996 which will be rounded to 3.58 when it is printed


#     @staticmethod
#     def from_sum(a, b):
#         return FixedFloat(a + b)

# print(FixedFloat(5.678)) # this will call the __repr__ method of the FixedFloat class and it will print <FixedFloat 5.68>
# print(FixedFloat.from_sum(1.234, 2.345)) # this will call the from_sum method of the FixedFloat class and it will
# print <FixedFloat 3.58> since it will add 1.234 and 2.345 and then it will create a new FixedFloat object with the amount of 3.5799999999999996 which will be rounded to 3.58 when it is printed

    @classmethod
    def from_sum(cls, a, b):
        return cls(a + b)

class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = "€"

    def __repr__(self):
        return f"<Euro {self.amount:.2f}{self.symbol}>"

print(Euro(5.678)) # this will call the __repr__ method of the Euro class and it will print <Euro 5.68€>
print(Euro.from_sum(1.234, 2.345)) # this will call the from_sum method of the FixedFloat class and it will print <Euro 3.58€> since it will add 1.234 and 2.345 and then it will create a new Euro object with the amount of 3.5799999999999996 which will be rounded to 3.58 when it is printed
