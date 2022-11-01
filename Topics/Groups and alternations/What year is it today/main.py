import re

template = r"(\d{1,2}[\./]){2}(\d{4})"
string = input()
match = re.match(template, string)
print(match.group(2) if match else None)