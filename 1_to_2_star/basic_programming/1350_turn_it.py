import math

tc = int(input())

for _ in range(tc):
    u, v, a, s = map(
        int,
        input().split(),
    )
    if u**2 > 2*a*s:
        if v >= math.sqrt(u**2 - 2*a*s):
            print("Yes")
        else:
            print("No")
    else:
        # caar will come to hold
        print("Yes")
