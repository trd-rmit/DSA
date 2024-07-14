from collections import Counter

t = int(input())

for _ in range(t):
    s = input()
    n = len(s)
    s1 = s[:n//2]
    s2 = s[-1:-(n//2+1):-1]
    result = "YES" if Counter(s1) == Counter(s2) else "NO"
    print(result)
