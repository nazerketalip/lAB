import re
s = input()
n = re.compile('[a-z]+[a-z]+')
result = n.findall(s)
print(result)
