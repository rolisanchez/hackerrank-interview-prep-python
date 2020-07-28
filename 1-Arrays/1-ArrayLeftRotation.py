#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    rotations = d % len(a)
    print("rotations = ", rotations)
    print("a[rotations:]+a[0:rotations] = ", a[rotations:]+a[0:rotations])
    return a[rotations:] + a[0:rotations]
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nd = input().split()

    # n = int(nd[0])
    n = 5
    # d = int(nd[1])
    d = 4

    arr = "1 2 3 4 5"
    
    # a = list(map(int, input().rstrip().split()))
    a = list(map(int, arr.rstrip().split()))
    print("a = ", a)
    result = rotLeft(a, d)
    print("Result = ", result)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
