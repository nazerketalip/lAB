def palin(s):
    if s == s[::-1]:
        return True
    return False
s = input()
print(palin(s))