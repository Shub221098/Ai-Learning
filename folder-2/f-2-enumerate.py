# Folder 2: Video - 17 : enumerate function in python
# Like zip, we can enumerate to turn a sequence like a list or a tuple

friends = ["Rolf", "John", "Anna"]
counter = 0

for friend in friends:
    print(counter)
    print(friend)
    counter = counter + 1

for counter, friend in enumerate(friends, start=1):
    print(counter, friend)

print(list(enumerate(friends)))
print(dict(enumerate(friends)))
print(list(zip([0, 1, 2], friends)))