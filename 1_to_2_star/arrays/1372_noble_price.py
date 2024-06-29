tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())
    arr = list(map(
        int,
        input().split(),
    ))
    if len(set(arr)) == m:
        print("No")
    else:
        print("Yes")
