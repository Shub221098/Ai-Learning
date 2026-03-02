# Folder 9: Video - 1 : Generators in python


def hundred_numbers():
    i = 0
    while i < 100:
        yield i
        i += 1
    
print(hundred_numbers()) # <generator object hundred_numbers at 0x000001B2C9F8B0D0>
g = hundred_numbers()
print(next(g)) # 0


my_range_obj = range(10)
# next(my_range_obj) # 0 throw error

print(my_range_obj) # range(0, 10) 

print(list(g)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
