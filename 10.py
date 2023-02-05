def uniq(lst):
    x = 0
    for a in lst:
        x = lst.count(a)
        if x == 1:
            print(a)


n = int(input())
lst = []
for i in range(n):
    x = input()
    lst.append(x)
uniq(lst)


