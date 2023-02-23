import re
s = input()
n = re.compile('[\w\.,]+@[\w\.,]+\.\w+')
result = n.findall(s)
print(result)