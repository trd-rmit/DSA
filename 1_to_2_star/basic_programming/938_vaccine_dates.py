total_test_cases = int(input())

for _ in range(total_test_cases):
    d, l, r = map(int, input().split())
    if l <= d <= r:
        print("Take second dose now")
    elif d < l:
        print("Too Early")
    else:
        print("Too Late")
