import re
s = input()
n = re.compile('a.*?b$')
result = n.findall(s)
print(result)