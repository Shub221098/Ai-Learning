# Folder 5: Video - 4: Raise Errors in Python


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

    # def add_car(self, car):
    #    raise NotImplementedError("This method is not implemented yet.")
    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f'Tried to add a `{car.__class__.__name__}` to the garage, but you can only add `Car` objects.')
        self.cars.append(car)

# ford = Garage()
# ford.add_car("Fiesta") # WE get error because the method is not implemented yet. We can use this to remind us to implement the method later.
# print(len(ford))

ford = Garage()
ford.add_car("Fiesta") # We get error because we are trying to add a str instead of a Car object. This is a type error, and we can use this to remind us to only add Car objects to the garage.
# print(len(ford))
car = Car("Ford", "Fiesta")
ford.add_car(car) # This works because we are adding a Car object to the garage.
print(len(ford)) # length = 1 because we have added one car to the garage.