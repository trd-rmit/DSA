tc = int(input())

for _ in range(tc):
    n = int(input())
    arr = list(map(
        int,
        input().split(),
    ))
    arr.sort(reverse=True)
    median_index = n//2
    if n%2 == 0:
        median = (arr[median_index] + arr[median_index - 1])/2
    else:
        median = arr[median_index]
    ans = 0
    for score in arr:
        if score < median:
            break
        ans += 1
    print(ans)
