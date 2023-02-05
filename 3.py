def solve(heads, legs):
    for i in range(legs+1):
         j = heads - i
         if i*2 + 4 * j == legs:
                return i, j
heads = int(input())
legs = int(input())
print(solve(heads, legs))
