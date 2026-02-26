# Folder 2: Video - 16 : zip function in python

friends = ["Rolf", "Bob", "Charlie", "Jen"]
time_since_seen = [3, 7, 15, 11]

long_timers = {
    friends[i]: time_since_seen
    for i in range(len(friends))
}

print(long_timers)

# Another way to make it dict

long_timers = dict(zip(friends, time_since_seen))
print(long_timers) # <zip ojbect at fasdfdon>

# Another way
long_timers = list(zip(friends, time_since_seen, [1, 2, 3, 4, 5]))
print(long_timers) # [('Rolf', 3, 1), ("Bob", 7, 2), ("Jan", 15, 3), ("Anne", 11, 4)]

