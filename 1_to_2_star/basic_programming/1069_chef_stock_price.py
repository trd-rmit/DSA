tc = int(input())

for _ in range(tc):
    s, a, b, c = map(
        int,
        input().split(),
    )
    if a <= s + s*c/100 <= b:
        print("YES")
    else:
        print("NO")
