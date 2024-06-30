#!/bin/python3


def miniMaxSum(arr):
    # Write your code here
    total_sum = sum(arr)
    min_4_sum = total_sum
    max_4_sum = 0
    for val in arr:
        sum_excluding_val = total_sum - val
        if sum_excluding_val > max_4_sum:
            max_4_sum = sum_excluding_val
        if sum_excluding_val < min_4_sum:
            min_4_sum = sum_excluding_val
    print(min_4_sum, max_4_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
