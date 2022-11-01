import re

template = "(Value|Name|Type)Error"
string = input()
match = re.match(template, string)
print(match.group(1) if match else None)