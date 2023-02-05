def histogram(lst):
    for i in lst:
        print(i*"*")



n = int(input())
lst = []
for i in range(n):
    x = int(input())
    lst.append(x)

histogram(lst)
