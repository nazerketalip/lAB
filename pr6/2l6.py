import re
s = input()
n = ['@mail.ru', '@yakoo.com', '@bk.ru']
m = ['@gmail.com', '@outlook.com', "@kbtu.kz"]
for i in range(len(n)):
    res1 = re.sub(n[i], m[i], s)
    print(res1)
    continue