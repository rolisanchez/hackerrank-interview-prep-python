
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    used = [False] * len(arr)

    for i in range(n):
        print("** i is ", i, " ***")
        if not used[i]:
            used[i] = True
            j = arr[i] - 1
            while j != i:
                print("j = ", j)
                used[j] = True
                swaps += 1
                j = arr[j] - 1
    return swaps
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())
    n = 4
    arrstr = "4 3 1 2"
    # n = 5
    # arrstr = "2 3 4 1 5"
    # n = 7
    # arrstr = "1 3 5 2 4 6 7"
    
    # arr = list(map(int, input().rstrip().split()))
    arr = list(map(int, arrstr.rstrip().split()))

    res = minimumSwaps(arr)
    print("Result is = ", res)
    # fptr.write(str(res) + '\n')

    # fptr.close()
