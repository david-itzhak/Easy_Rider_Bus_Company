import re

string = input()
elements_list = re.findall('(?<=<li>).+?(?=</li>)', string)
print(*elements_list, sep='\n')