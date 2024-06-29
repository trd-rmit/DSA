tc = int(input())

for _ in range(tc):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(sum(arr)%k)
