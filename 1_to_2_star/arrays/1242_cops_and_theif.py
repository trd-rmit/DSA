t = int(input())

for _ in range(t):
    m, x, y = map(
        int,
        input().split(),
    )
    cops = list(map(
        int,
        input().split(),
    ))
    cop_length = x * y
    secure = [0 for i in range(100)]
    for cop in cops:
        cop_min = max(cop - cop_length, 1)
        cop_max = min(cop + cop_length, 100)
        for i in range(cop_min - 1, cop_max):
            secure[i] = 1
    print(secure.count(0))
