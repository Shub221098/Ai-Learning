# Folder 9: Video -6 : Filter in python
# Use filter function when you are working with different languages


def starts_with_r(friend):
    reutrn friend.startwith('R')

friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Marry']

start_with_r = filter(starts_with_r, friends) # arg 1: function that return True/False


print(next(start_with_r))
print(next(start_with_r))
print(next(start_with_r))

# filter function using lambda
start_with_r2 = filter(lambda friend: x.startswith('R'), friends)

# Genertor way to write this
another_starts_with_r = (f for f in friends if f.startswith('R'))

def my_custom_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i