import re

string = input()
match_object = re.match('Good (morning|afternoon|evening)', string)
print(match_object.group() if match_object else "No greeting!")