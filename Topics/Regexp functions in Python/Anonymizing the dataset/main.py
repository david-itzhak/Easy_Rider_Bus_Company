import re

string = input()
string = re.sub(r'^@\w+', '<AUTHOR>', string)
string = re.sub(r'@\w+', '<HANDLE>', string)
print(string)