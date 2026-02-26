# Folder 1: Video - 18 : sets in Python

art_friends = {"Rolf", "Anne"}
science_friends = {"Jen", "Charlie"}

art_friends.add("Jen")

print(art_friends) # {"Rolf", "Anne", "Jen"}

art_friends.add("Jen")
print(art_friends) # {"Rolf", "Anne", "Jen"}

art_friends.remove("Jen")

# Advanced set operations

art_friends1 = {"Rolf", "Anne", "Jen"}
science_friends1 = {"Jen", "Charlie"}

art_but_not_science = art_friends1.difference(science_friends1)
science_but_not_art = science_friends1.difference(art_friends1)

print(art_but_not_science) # {"Anne", "Rolf"}
print(science_but_not_art) # {"Charlie"}

# members who are not in both
not_in_both = art_friends.symmetric_difference(science_friends1)
print(not_in_both) # {"Anne", "Rolf", "Charlie"}


# members who are same in both
art_and_science = art_friends1.intersection(science_friends1)

# all members who are not same in both
all_friends = art_friends.union(science_friends)
print(all_friends) # {"Anne", "Rolf", "Jen", "Charlie"}

