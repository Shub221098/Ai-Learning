# Folder 2: Video - 20 : arguments and paremeters in python


car = {
    "make": "Ford",
    "model": "Fiesta",
    "mileage": 23000,
    "fule_consumed": 460
}

mpg = car["mileage"] / car["fule_consumed"]
name = f"{car['make']} {car['model']}"
print(f"{name} does {mpg} miles per gallon.")


# Now we create a function as this task is done many times
def calculate_mpg():
    car = {
        "make": "Ford",
        "model": "Fiesta",
        "mileage": 23000,
        "fule_consumed": 460
    }

    mpg = car["mileage"] / car["fule_consumed"]
    name = f"{car['make']} {car['model']}"
    print(f"{name} does {mpg} miles per gallon.")

calculate_mpg()

# Another way

car = {
    "make": "Ford",
    "model": "Fiesta",
    "mileage": 23000,
    "fule_consumed": 460
}

def calculate_mpg(car_to_calculate):
    mpg = car_to_calculate["mileage"] / car_to_calculate["fule_consumed"]
    name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
    print(f"{name} does {mpg} miles per gallon.")

calculate_mpg(
    {
        "make": "Ford",
        "model": "Fiesta",
        "mileage": 23000,
        "fule_consumed": 460
    }
)

# Another one

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

def calculate_mpg(car_to_calculate):
    mpg = car_to_calculate["mileage"] / car_to_calculate["fule_consumed"]
    name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
    print(f"{name} does {mpg} miles per gallon.")

for car in cars:
    calculate_mpg(car)
