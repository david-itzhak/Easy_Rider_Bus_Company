import re

string = input()
# your code here

capitalized_word_pattern = '[A-Z][a-zA-Z]+'
digits_pattern = r'\d+'
capitalized_words = re.findall(capitalized_word_pattern, string)
print('Capitalized words:', ', '.join(capitalized_words))
digits = re.findall(digits_pattern, string)
print('Digits:', ', '.join(digits))

