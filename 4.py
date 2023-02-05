def filter_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


lst = []
lst1 = []
a = int(input())
for i in range(a):
    x = int(input())
    if filter_prime(x) == True:
        lst1.append(x)
print(lst1)
