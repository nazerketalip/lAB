import re
s = input()
n = re.compile('[A-Z][^A-Z]*')
result = n.findall(s)
print(result)