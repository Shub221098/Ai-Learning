# Folder 2: Video - 13 : list-comprehension in python


numbers = [0, 1, 2, 3, 4 ]
doubled_numbers = []

for number in numbers:
    doubled_numbers.append(number * 2)

print(doubled_numbers)


# Now the above thing with list comprehension

doubled_numbers = [number * 2 for number in numbers]

print(doubled_numbers)

doubled_numbers = [number * 2 for number in range(5)]
print(doubled_numbers)

# want to create a new list which contain string describing your ages.
friend_ages = [22, 21, 35, 47]
age_strings = [f"My friend is {age} years old" for age in friend_ages]

# Want a list of lowercase letters from below list
names = ["Rolf", "Bob", "Jen"]
name_with_lower_case = [name.lower() for name in names]
print(name_with_lower_case)

# Want to enter firends name and check whether it is in friends list or not
friend = input("Enter your friend name: ")
friends = ["Rolf", "Bob", "Jen", "Charlie", "Anne"]
friends_lower = [name.lower() for name in friends]

if friend.lower() in friends_lower:
    print(f"{friend.title()} is one of your friends.")