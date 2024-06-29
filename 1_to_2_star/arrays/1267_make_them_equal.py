tc = int(input())

for _ in range(tc):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max(arr) - min(arr))
