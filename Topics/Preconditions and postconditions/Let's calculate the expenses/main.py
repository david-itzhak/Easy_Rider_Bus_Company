import re

expenses = sum(int(x) for x in re.findall(r'(?<=\$)\d+', input()))
print(f'This week you have spent: {expenses} dollars')
