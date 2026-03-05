# Folder 10: Video - 2 : Argument Mutability in python

friends_last_seen = {
    'Rolf': 31,
    'Jen': 27,
    'Anne': 1
}

def see_friend(friends, name):
    print(friends is friends_last_seen) # is compare the ids and here comes true
    print(id(friends))
    friends[name] = 0

print(id(friends_last_seen)) # same id come
print(id(friends_last_seen['Rolf'])) # different id - before modified
see_friend(friends_last_seen, 'Rolf') # same id come
print(id(friends_last_seen['Rolf']))  # different id - after modified - mutability in action
print(id(friends_last_seen)) # same id come 


print(friends_last_seen['Rolf']) # it comes 0

age = 20

def increase_age(current_age):
    current_age = current_age + 1

id(id(age)) # same id
increase_age(age)
id(id(age)) # same id

primes = [2, 3, 5]

print(id(primes))

primes += [7, 11] # primes = primes.__iadd__([7, 11]) # it modifies the list and id will be same
primes = [2, 3, 5] + [7, 11] # primes = primes.__add__([7, 11]) # different ids comes as it create new list
primes = primes + [7, 11]# primes = primes.__add__([7, 11]) # different ids comes as it create new list

print(id(primes))