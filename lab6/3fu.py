import itertools
soz = str(input())
teris_soz = ''.join(reversed(soz))
if teris_soz == soz:
    print("YES")
else:
    print("NO")