tc = int(input())

for _ in range(tc):
    s = input()
    ans = 0
    if s[0] == '0':
        allowed_flag = '0'
        ans += 1
    else:
        allowed_flag = '1'
    for door in s[1:]:
        if door != allowed_flag:
            ans += 1
            allowed_flag = door
    print(ans)
