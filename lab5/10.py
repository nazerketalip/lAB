import re
s = input()
n = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
result = re.sub('([a-z0-9])([A-Z])', r'\1_\2', n)
print(result.lower())
