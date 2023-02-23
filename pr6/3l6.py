n, m, x, y = 0, 0, 0, 0
s = input()
specialchar = "~`!@#$%^&*()_-+=\|?/.,<>"
digits = "1234567890"
if (len(s) >= 8 and len(s)<=15):
    for i in s:
        if i == i.lower():
            n += 1
        if i == i.upper():
            m += 1
        if i in digits:
            x += 1
        if i in specialchar:
            y += 1
if (n>=1 and m >= 1 and x >= 1 and y >= 1 and n + y + x + y == len(s)):
    print("Valid")
else:
    print("Invalid")