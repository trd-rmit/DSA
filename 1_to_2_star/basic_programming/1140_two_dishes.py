tc = int(input())

for _ in range(tc):
    n, a, b, c = map(int, input().split())
    if b >= n and a + c >= n:
        print("YES")
    else:
        print("NO")
