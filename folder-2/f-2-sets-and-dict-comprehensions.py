# Folder 2: Video - 15 : sets and dictionary comprehensions in python


friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = {n.lower() for n in friends}
guests_lower = {n.lower() for n in guests}
present_friends = friends_lower.intersection(guests_lower)

present_friends = {name.title() for name in present_friends}


# 

friends = ["Rolf", "ruth", "charlie", "Jen"]
time_since_seen = [3, 7, 15, 11]

long_timers = {
    friends[i]: time_since_seen
    for i in range(len(friends))
}

print(long_timers) # {"Rolf": 3, "Ruth": 7, "Charlie": 15, "Jen": 11}

