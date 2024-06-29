tc = int(input())

required_ans = sum([i for i in range(1,8)])
for _ in range(tc):
    ans = 0
    min_problems = 0
    total_problems = int(input())
    arr = list(map(int, input().split()))
    for prob_level in arr:
        if 1 <= prob_level <= 7:
            ans += prob_level
        min_problems += 1
        if ans == required_ans:
            break
    print(min_problems)
