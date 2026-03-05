# Folder 10: Video - 12 & 13 & 14 : Regular expression in python

#  .  ->   "anything"- letters, numbers, symbols... but not newlines
#  +  ->   "one or more of"
#  *  ->   "zero or more of"
#  ?  ->   "zero or one of"

import re

email = 'jose@tecladocode.com'
expression = '[a-z\.]+'

matches = re.findall(expression, email)
print(matches)

name = matches[0]
domain = f'{matches[1]}.{matches[2]}'
print(name) # jose
print(domain) # tecladocode.com

price = 'Price: $18,649.50'
expresssion = 'Price: \$([0-9]*\.[0-9]*)'

matches = re.search(expression, price)
print(matches.group(0))
print(matches.group(1))

price_without_comma = matches.group(1).replace(',', '')
price_number = float(price_without_comma)

print(price_number)