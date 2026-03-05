# Folder 10: Video - 9 : Timezones in python

from datetime import datetime

print(datetime.now()) # it does not give timezone called "naive"


from datetime import datetime, timezone

print(datetime.now(timezone.utc)) # aware

# Folder 10: Video - 10 : Dates and times in python

from datetime import datetime

print(datetime.now()) # current time of our operating system

today = datetime.now(timezone.utc)
tommorrow = today + timedelta(days-1)

print(today)
print(tommorrow)

print(today.strftime('%d-%m-%Y %H:%M:%S')) # string format - 15-02-2026 23:59:45

user_date = input('Enter the date in YYYY-mm-dd format: ')
user_date = datetime.strptime(user_date, '%Y-%m-%d') # string parse time

print(user_date)


# PDF


# This syntax below can be used in the  strftime  and  strptime  methods, like so:
# import datetime 
# now = datetime.datetime.now() 
# print(now.strftime(‘%d-%m-%Y’))  # 13-03-2018 
# print(now.strftime(‘%A, %B %d, %Y’)  # Tuesday, March 13, 2018 
 
# user_date = input(‘Enter the current date as %Y-%m-%d: ‘) 
# print(datetime.datetime.strptime(user_date, “%Y-%m-%d”))

# Code Meaning Example
# %A - Day of the week as text - Monday
# %d - Day of the month from 01 to 31 - 17
# %B - Month name as text - October
# %m - Month of the year from 01 to 12 - 7
# %Y - Year with century - 2016
# %H - Hour from 00 to 23 - 15
# %I - Hour from 00 to 12 - 7
# %p - Equivalent of AM or PM in the current language - AM
# %M - Month from 01 to 12 - 10
# %S - Seconds from 00 to 59 - 54
# %x - Date representation in the current language - 06/10/15
# %X - Time representation in the current language - 19:54:22

# import datetime 
 
# users = [] 
 
# new_user = { 
#   ‘name’: input(‘Enter your name: ‘) 
#   ‘location’: input(‘Enter your location: ‘) 
#   ‘registered’: datetime.datetime.now(datetime.timezone.utc) 
# } 
 
# users.append(new_user)

# import datetime 
 
# users = [] 
 
# name = input(‘Enter your name: ‘) 
# location = input(‘Enter your location: ‘) 
# registered = datetime.datetime.now(datetime.timezone.utc) 
 
 
# new_user = { 
#   ‘name’: name 
#   ‘location’: location 
#   ‘registered’: registered 
# } 
 
# users.append(new_user)

# import datetime 
 
# class User: 
#   def __init__(self, username, password): 
#     self.username = username 
#     self.password = password 
#     self.registered = datetime.datetime.now(datetime.timezone.utc)