test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    report = input()
    ans = 0
    for i in report:
        if i == 'H':
            ans += 1
        elif i == 'T':
            ans -= 1
        if ans < 0 or ans > 1:
            print("Invalid")
            break
    else:
        if ans != 0:
            print("Invalid")
        else:
            print("Valid")
