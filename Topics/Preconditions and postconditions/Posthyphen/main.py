import re

string = input()
print(re.search('(?<=-).+', string).group())