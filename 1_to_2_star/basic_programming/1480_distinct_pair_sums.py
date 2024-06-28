tc = int(input())

for _ in range(tc):
    l, r = map(
        int,
        input().split(),
    )
    print(2*r-2*l + 1)
