total_test_cases = int(input())

for _ in range(total_test_cases):
    n, s = map(int, input().split())
    t1 = min(n, s)
    t2 = s - t1
    print(t1 - t2)
