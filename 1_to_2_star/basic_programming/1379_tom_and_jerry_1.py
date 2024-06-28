tc = int(input())

for _ in range(tc):
    a, b, c, d, k = map(
        int,
        input().split(),
    )
    dist = abs(a-c) + abs(b-d)
    if dist > k:
        print("NO")
    else:
        remaining_dist = k - dist
        if remaining_dist % 2 == 0:
            print("YES")
        else:
            print("NO")
