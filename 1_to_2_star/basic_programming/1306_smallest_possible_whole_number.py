tc = int(input())

for _ in range(tc):
    n, k = map(int, input().split())
    if k == 0:
        print(n)
    else:
        print(n%k)
