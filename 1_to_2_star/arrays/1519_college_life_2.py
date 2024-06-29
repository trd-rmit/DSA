tc = int(input())

for _ in range(tc):
    seasons = int(input())
    intros = list(map(
        int,
        input().split(),
    ))
    ans = 0
    for s in range(seasons):
        eps = list(map(
            int,
            input().split(),
        ))
        ans += eps[1]
        for l in eps[2:]:
            ans += l - intros[s]
    print(ans)
