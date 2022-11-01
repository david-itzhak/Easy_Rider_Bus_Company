import re

print('Thank you!' if re.compile('[a-zA-Z]').match(input()) else 'Oops! The username has to start with a letter.')