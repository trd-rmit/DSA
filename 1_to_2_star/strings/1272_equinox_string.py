t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())
    ans = 0
    test_set = set("EQUINOX")
    for _ in range(n):
        s = input()
        if s[0] in test_set:
            ans += a
        else:
            ans -= b
    if ans > 0:
        print("SARTHAK")
    elif ans < 0:
        print("ANURADHA")
    else:
        print("DRAW")
