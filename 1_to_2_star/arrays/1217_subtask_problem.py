tc = int(input())

for _ in range(tc):
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    points = 0
    if all(arr[:m]):
        points += k
        if all(arr[m:]):
            points = 100
    print(points)
