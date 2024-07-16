t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    no_ones = s.count("1")
    ans = (no_ones * (no_ones + 1))//2
    print(ans)
