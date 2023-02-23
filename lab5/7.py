import re
s = input()
result = ''.join(x.capitalize() or '_' for x in s.split('_'))
print(result)