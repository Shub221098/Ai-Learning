# Folder 6: Video - 9 :  Using the with syntax in python

import json

file = open('friend_json','r')
file_contents = json.load(file) # reads file and turn it into dictionary

file.close()

# print(file_contents['friends'][0]) {"name" : "Jose", "degree": "Applied Computing"  }

cars = [
    {'make':'Ford','modal':'Fiesta'},
    {'make':'Ford','modal':'Focus'},
]

file = open('friend_json','w')
json.dump(cars,file)
file.close()


## dumps allows you to turn dictionary into string
## loads allows you to turn string into dictionary
## jso allows you to ue dict and

my_json_string = '[{"name":"alfa","released":1985}]'

incorrect_car = json.loads(my_json_string)

print(incorrect_car[0])

# Using with 

with open('friend_json','r') as file:
    file_contents = json.load(file)
print(file_contents['friends'][0])

cars = [
    {'make':'Ford','modal':'Fiesta'},
    {'make':'Ford','modal':'Focus'},q
]

with open('cars_json','w') as file:
    json.dump(cars,file)

my_json_string = '[{"name":"alfa","released":1985}]'

incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])