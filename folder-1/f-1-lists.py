# Folder 1: Video - 16 : Lists in Python

friend1 = "Rolf"
friend2 = "Bob"
friend3 = "John"

print(friend1)
print(friend2)

# So insted of printing differently we use lists

friends = ["Rolf", "Anne"]
friends2 = [["Rolf", 24], ["Anne", 34], ["John", 25]]

friends.append("Jen")
friends.remove("Rolf")

print(friends[0])
print(friends[2])

print(len(friends)) # Get length of lists
print(friends[0][0]) # To get Rolf
print(friends[1][1])


friends3 = [
    ["Rolf", 24],
    ["Anne", 34],
    ["John", 25],
    ["Charlie", 51],
    ["Jen", 47]
]

friends3.remove(["Anne", 34])
friends3.remove("Anne") # Throw error

