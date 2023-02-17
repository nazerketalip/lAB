def even(n):
    for i in range(n+1):
        if i % 2 == 0:
            if i < n-1:
                print(i,end=',')
            else:
                print(i)


n=int(input())
even(n)
