tc = int(input())

for _ in range(tc):
    a, b, c = map(int, input().split())
    if a > b:
        if b > c:
            print(a+b)
        else:
            print(a+c)
    else:
        if a > c:
            print(b+a)
        else:
            print(b+c)
