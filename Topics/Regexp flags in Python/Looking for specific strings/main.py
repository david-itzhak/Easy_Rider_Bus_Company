import re

string = input()
match = re.match('b.*l', string, flags=re.IGNORECASE)
print(match.group() if match else 'No match')