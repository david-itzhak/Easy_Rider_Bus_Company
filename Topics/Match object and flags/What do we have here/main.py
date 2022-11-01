import re
import string

template = r'... Jude'
match = re.match(template, input())
print(match.group() if match else None)