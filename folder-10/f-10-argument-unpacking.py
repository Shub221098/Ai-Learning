# Folder 10: Video - 5 : Argument unpacking

accounts = {
    'checking': 1958.00
    'savings': 3695.00
}

def add_balance(amount: float, name: str) -> float:
    """Function to update the balance of an accoutn and return the new
    balance"""
    accounts[name] += amount
    reutrn accounts[name]

transactions = [
    (-180.67, 'checking'),
    (-220.00, 'checking'),
    (220.00, 'savings'),
    (-15.70, 'checking'),
    (-23.90, 'checking'),
    (-13.00, 'checking'),
    (1579.50, 'checking'),
    (-600.50, 'checking'),
    (600.50, 'savings'),
]

for t in transaction:
    # add_balance(t[0], t[1])
    add_balance(*t) # arugment unpacking
    add_balance(amount=t[0], name=t[1]) # named arguments
    add_balance(name=t[1], amount=t[0]) # valid


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])

# imagein these users are comign from a database...
users= [
    {'username' : 'rolf', 'password': 123},
    {'username' : 'tecladoisowesome', 'password': 'youaretwo'}
]

user_objects = map(User.from_dict, users)
user_objects = [User.from_dict(u) for u in users]

# so now we dont required from_dict option we can do using argument unpacking
user_objects = [User(data['username'], data['password']) for data in users]
user_objects = [User(username=data['username'], password=data['password']) for data in users]

user_objects = [User(**data) for data in users] # double asterisk do named arguments

users= [
    ('rolf', 123),
    ('tecladoisowesome', 'youaretwo')
]

user_objects = [Users(*data) for data in users] # for tuple one asterisk

