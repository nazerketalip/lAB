import re
s = input()
n =re.compile('ab*?')
result = n.findall(s)
print(result)