# Folder 2: Video - 5 : Destructuring in python

currencies = 0.8, 1.2
usd, err = currencies


friends = [("Rolf", 25), ("Bob", 37),("Anne", 31), ("Charlie", 22)]


for name, age in friends:
    print(f"{name} is {age} years old.")

# Folder 2: Video - 6 : Iterate over dictionaries

friend_ages = {"Rolf": 25, "Anne": 27, "Charlie": 31, "Bob": 22}

for name in friend_ages:
    print(f"{name}") # only key comes

for age in friend_ages.values():
    print(f"{age}")

for name, age in friend_ages.items():
    print(f"{name} is {age} years old.") 