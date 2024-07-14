t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    x, y = map(int, input().split())
    for _ in range(n):
        marks = input()
        p = marks.count('P')
        f = marks.count('F')
        if f >= x or (f == x - 1 and p >= y):
            print("1", end="")
        else:
            print("0", end="")
    print()
