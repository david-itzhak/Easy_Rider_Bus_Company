import re

string = input()
template = '<START>(.*)<END>'
result_list = re.findall(template, string)
print(result_list[0] if result_list else None)
