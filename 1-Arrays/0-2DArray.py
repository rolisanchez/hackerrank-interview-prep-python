import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    # print("arr = ", arr) 
    # print("arr[0] = ", arr[0]) 
    # print("arr[0][3] = ", arr[0][3]) 
    sums = []
    for row in range(4):
        # print("row = ", row)
        for col in range(4):
            sum = arr[0+row][0+col]
            sum += arr[0+row][1+col]
            sum += arr[0+row][2+col]
            sum += arr[1+row][1+col]
            sum += arr[2+row][0+col]
            sum += arr[2+row][1+col]
            sum += arr[2+row][2+col]
            sums.append(sum)
            # print("col = ", col)
    print("sums = ", sums)
    return max(sums)
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []
    lines = []
    lines.append("1 1 1 0 0 0")
    lines.append("0 1 0 0 0 0")
    lines.append("1 1 1 0 0 0")
    lines.append("0 0 2 4 4 0")
    lines.append("0 0 0 2 0 0")
    lines.append("0 0 1 2 4 0")
    
    for i in range(6):
        # # arr.append(list(map(int, input().rstrip().split())))
        # print("lines[i] = ", lines[i])
        arr.append(list(map(int, lines[i].rstrip().split())))

    result = hourglassSum(arr)
    print("Result is = ", result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
