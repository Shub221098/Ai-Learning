# Folder 2: Video - 21 : functions and return values in python

cars = [
    {
        "make": "Ford",
        "model": "Fiesta",
        "mileage": 23000,
        "fule_consumed": 460
    },
    {
        "make": "Ford",
        "model": "Fiesta",
        "mileage": 49000,
        "fule_consumed": 460
    },
    {
        "make": "Mazda",
        "model": "Fiesta",
        "mileage": 17000,
        "fule_consumed": 460
    },
    {
        "make": "Mini",
        "model": "Fiesta",
        "mileage": 31000,
        "fule_consumed": 460
    }
]

def calculate_mpg(car):
    mpg = car["mileage"] / car["fule_consumed"]
    return mpg


def car_name(car):
    name = f"{car['make']} {car['model']}"
    return name


def print_car_info(car):
    name = car_name(car)
    mpg = calculate_mpg(car)
    
    print(f"{name} does {mpg} miles per gallon.")


for car in cars:
    print_car_info(car)