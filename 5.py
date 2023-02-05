from itertools import permutations
def permit(s):
    result = permutations(s)
    for i in result:
        print(i)

s = input()
permit(s)