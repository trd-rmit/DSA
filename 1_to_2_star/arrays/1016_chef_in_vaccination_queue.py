tc = int(input())

for _ in range(tc):
    n, p, x, y = map(
        int,
        input().split(),
    )
    arr = list(map(
        int,
        input().split(),
    ))
    ans = 0
    for i in range(p):
        ans += y if arr[i] == 1 else x
    print(ans)
