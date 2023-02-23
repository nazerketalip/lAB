import re
s = input()
n = re.compile('[A-Z]+[a-z]+')
result = n.findall(s)
print(result)
