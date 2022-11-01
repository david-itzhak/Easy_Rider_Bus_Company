import re

template = r'are you ready??.?.?'
match_object = re.match(template, input())
print(len(match_object.group()) if match_object else 0)
