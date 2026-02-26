# Folder 1: Video - 21 : Python dictionaries

friend_ages = {"Rolf" : 24, "Adam": 30, "Anne": 27}
friend_ages["Bob"] = 20
friend_ages["Rolf"] = 25

# do not a duplicate key but update value of key
print(friend_ages)


friends = (
    {"name" : "Rolf Smith", "age": 24},
    {"name" : "Adam Wool", "age": 30},
    {"name" : "Rolf Smith", "age": 27}
)

print(friends[0]["name"])
print(friends[1]["name"])
print(friends[2]["name"])


# dict is used to convert date into dictionary

friends = [("Rolf", 24), ("Adam", 30), ("Anne", 27)]

friends_ages = dict(friends)
print(friends_ages) # { "Rolf": 24, "Anne" : 30, "Anne": 27 }