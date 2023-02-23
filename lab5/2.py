import re

s = input()
result = re.compile('ab{2,3}')
m = result.findall(s)
print(m)
