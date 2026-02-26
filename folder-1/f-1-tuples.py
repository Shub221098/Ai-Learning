# Folder 1: Video - 17 : tuples in python

# this is also tuple
short_tuple = "Rolf", "Bob"
# and this is also tuple
a_bit_clearer = ("Rolf", "Bob")


# It is not a tuple, by adding comma it consider tuple
not_a_tuple = "Rolf"
a_tuple_with_comma = "Rofl",

# Want to create of list of tuples
tuple_in_list = [("Rolf", "Bob")]


# Add new element in a tuple
friends = ("Rolf", "Bob", "Anne")
friends = friends + ("Jen")
print(friends) # ("Rolf", "Bob", "Anne", "Jen")

# In List we can append element but in tuple create another tuple and then add both of them