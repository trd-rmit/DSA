#!/bin/python3

# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr, n):
    # Write your code here
    arr_value_counts = {
        0: 0,
        1: 0,
        -1: 0,
    }
    for a in arr:
        if a > 0:
            arr_value_counts[1] += 1
        elif a < 0:
            arr_value_counts[-1] += 1
        else:
            arr_value_counts[0] += 1
    print(round(arr_value_counts[1]/n, 6))
    print(round(arr_value_counts[-1]/n, 6))
    print(round(arr_value_counts[0]/n, 6))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr, n)
