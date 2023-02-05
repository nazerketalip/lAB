def palinword(lst):
    lst.reverse()
    print(*lst)


s = input()
lst = s.split(" ")
palinword(lst)

