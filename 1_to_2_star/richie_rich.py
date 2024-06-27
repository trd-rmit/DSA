import math

total_test_cases = int(input())

for _ in range(total_test_cases):
    a, b, x = map(int, input().split())
    if a > b:
        print(0)
    else:
        print(math.ceil((b - a)/x))
