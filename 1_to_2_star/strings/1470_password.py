test_cases = int(input())

for _ in range(test_cases):
    password = input()
    length_password = len(password)
    l = [False] * 5
    for i, c in enumerate(password):
        if c >= 'a' and c <= 'z':
            l[0] = True
        if i != 0 and i != length_password - 1:
            if c >= 'A' and c <= 'Z':
                l[1] = True
            if c >= '0' and c <= '9':
                l[2] = True
            if c in {'@', '#', '%', '&', '?'}:
                l[3] = True
        if length_password >= 10:
            l[4] = True
    if sum(l) == 5:
        print("YES")
    else:
        print("NO")