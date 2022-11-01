import re

new_str = input()
print(re.findall(r'\w+', new_str, flags=re.I | re.A))
