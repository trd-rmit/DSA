tc = int(input())

for _ in range(tc):
    a, b, a1, b1, a2, b2 = map(
        int,
        input().split(),
    )
    s = {a, b}
    if s == {a1, b1}:
        print(1)
    elif s == {a2, b2}:
        print(2)
    else:
        print(0)
