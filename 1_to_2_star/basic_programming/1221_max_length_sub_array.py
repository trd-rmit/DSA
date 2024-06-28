tc = int(input())

for _ in range(tc):
    n = int(input())
    if (n*(n+1)/2) % 2 == 0:
        print(n)
    else:
        print(n-1)
