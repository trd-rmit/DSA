tc = int(input())

for _ in range(tc):
    w1, w2, x1, x2, m = map(
        int,
        input().split(),
    )
    increased_weight = w2 - w1
    if m * x1 <= increased_weight <= m * x2:
        print(1)
    else:
        print(0)
