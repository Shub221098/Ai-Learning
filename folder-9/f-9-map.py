# Folder 9: Video - 7 : Map in python
# when the people in team are using other programming languages is dependent on our python code then use map


friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Marry']

start_with_r = filter(starts_with_r, friends) # arg 1: function that return True/False

friends_lower = map(lambda x: x.lower(), friends)
friends_lower = [friends.lower() for friend in friends] # list comprehension
friends_lower = (friends.lower() for friend in friends) # Generators
print(next(friends_lower))

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])
    
users = [
    { 'username': "rolf", 'password': "123"}
    { 'username': "tecladoisawesome", "password": "youaretoo"}
]

users = [User.from_dict(user) for user in users]
users = map(User.from_dict, users)  # Here map is more readable.