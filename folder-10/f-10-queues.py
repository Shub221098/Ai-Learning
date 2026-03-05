# Folder 10: Video - 6 : Queues in python

"""A queue where you can add or remove
things either side is called in python
a "deque" or "double-ended queue."""


# Otherwise it's just a queue, add from one end and remove from other end.

# In a "stack" you add and remove the same end.



# Folder 10: Video - 7 : Some interesting python collections
"""
* counter
* defaultdict
* ordereddict
* namedtuple
* deque
"""

## Counter
from collections import Counter
device_temperatures = [13.5, 14.0, 14.0, 14.5, 14.5, 14.5, 15.0, 16,0]
temperature_counter = Counter(device_temperature)
print(temperature_counter[14.5]) # 3

print(Counter({'hello': 5, 'hi': 3})['hi'])

## defaultdict

my_dict = {'hello' : 5}
print(my_dict['hi']) # error hi doesn't exist

from collections import defaultdict

coworkers = [('Rolf', 'MIT'), ('Jen': 'Oxford'), ('Rolf', 'Cambridge'), ('Charlie', 'Manchester')]

# alma_maters = {}
alma_maters = defaultdict(list) #list()
for coworker,place in coworkers:
    alma_maters[coworker].append(place)

# for coworker in coworkers:
#     alma_maters[cowoker[0]] = []
#     alma_maters[coworker[0]].append(coworker[1])

# for coworker, place in coworkers:
#     if coworker not in alma_maters:
#         alma_maters[coworker] = []
#     alma_maters[coworker].append(place)

print(alma_maters['Rolf'])
print(alma_maters['Anne']) # it didnt throw error

alma_maters = default_factory = None
print(alma_maters['Anne']) # throw error

my_company = 'Teclado'

coworkers = ['Jen', 'Li', 'Charlie', 'Rhys']
other_coworkers = [('Rolf', 'Apple Inc.'), ('Anna', 'Google')]

coworker_companies = defaultdict(lambda: my_company)

for person, company in other_coworkers:
    coworker_companies[person] = company

print(coworker_companies(coworkers[0]))
print(coworker_companies['Rolf'])

## ordereddict

from collections import OrderedDict

o = OrderedDict()
o['Rolf'] = 6
o['Jose'] = 12
o['Jen'] = 3

print(o)

o.move_to_end('Rolf')
o.move_to_end('Jen', last=False)

print(o)

o.popitem()
print(o)


## namedtuple

from collections import namedtuple

account = ('checking', 1850.90)

print(account[0]) # name
print(account[1]) # balance

Account = namedtuple('Account', ['name', 'balance'])

account = Account('checking', 1850.90)
accountNameTuple = Account(*account)
print(accountNamedTuple._asdict()['balance'])

print(account.name) # checking
print(account) # Account(name : "checking", "balance": 1850.90)

## deque

from collections import deque

friends= deque(('Rolf', 'Charlie', 'Jen', 'Anna'))

friends.append('Jose')
friends.appendLeft('Anthony')

friends.pop()
friends.popleft()

