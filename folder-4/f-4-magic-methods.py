# Folder 4: Video - 7 : magic methods Python


class Student:
    def __init__(self, name, grades): # special method python cal it directly
        self.name = name
        self.grades = grades

movies = ["Matrix", "Finding Nemo", "Inception"]
print(movies.__class__) # str  # this will call the __clas__ method of the list class
print(movies.__len__()) # this will call the __len__ method of the list class
print(movies.__getitem__(0)) # this will call the __getitem__ method of the


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]

    def __repr__(self):
        return f'<Garage {self.cars}>'

    def __str__(self):
        return f"Garage with {len(self)} cars: {self.cars}"

ford = Garage()
ford.cars.append("Fiesta")
ford.cars.append("Focus")

print(len(ford)) #  it is same return 2 # this will call the __len__ method of the Garage class

print(ford[0]) # Garage.__getitem__(ford, 0)

for car in ford: # Garage.__getitem__(ford, 0), Garage.__getitem__(ford, 1)
    print(car)

print(ford) # this will call the __str__ method of the Garage class
print(repr(ford)) # this will call the __repr__ method of the Garage class