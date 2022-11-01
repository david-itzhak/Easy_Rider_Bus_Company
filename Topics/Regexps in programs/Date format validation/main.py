import re

string = input()
pattern = "[0-3][0-9]/[0-1][0-9]/[0-9]{4}"
qwer = re.match(pattern, string)
print(bool(qwer))