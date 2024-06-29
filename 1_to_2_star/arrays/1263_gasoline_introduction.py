tc = int(input())

for _ in range(tc):
    n = int(input())
    arr = list(map(int, input().split()))
    total_travel = arr[0]
    remaining_gas = arr[0]
    for i in range(1, n):
        if remaining_gas == 0:
            break
        total_travel += arr[i]
        remaining_gas += arr[i] - 1
    print(total_travel)
