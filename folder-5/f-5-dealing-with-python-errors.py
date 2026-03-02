# Folder 5: Video - 8 : Exception handling in python

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def __repr__(self):
        return f"< Car {self.make} {self.model}>"

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self ):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f'Tried to add a `{car.__class__.__name__}` to the garage, but you can only add `Car` objects.')
        self.cars.append(car)

ford = Garage()
fiesta = Car("Ford", "Fiesta")

if isinstance(fiesta, Car):
    ford.add_car(fiesta)
else:
    print("Your car was not a Car!")

# Instead of do above do this way
try:
    ford.add_car("Fiesta") # We get error because we are trying to add a str instead of a Car object. This is a type error, and we can use this to remind us to only add Car objects to the garage.
except TypeError as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Value error: {e}")
finally:
    print("This will always be executed.")
print(len(ford)) # length = 0 because we have not added any car to the


try:
    ford.add_car(fiesta) # This works because we are adding a Car object to the garage.
except TypeError as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Value error: {e}")
finally:
    print("This will always be executed.")

print(len(ford)) # length = 1 because we have added one car to the garage.

