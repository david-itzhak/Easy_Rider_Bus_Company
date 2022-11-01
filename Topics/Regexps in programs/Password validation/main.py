import re

password = input()
pattern = "[a-zA-Z0-9]{6,15}$"
result = re.match(pattern, password)
print('Thank you!' if result else 'Error!')
