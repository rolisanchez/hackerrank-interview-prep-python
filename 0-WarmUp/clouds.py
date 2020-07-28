#!/bin/python3

import math
import os
import random
import re
import sys

def jumpingOnClouds(c):
    currentPos = 0
    jumpCount = 0
    while currentPos < len(c)-1:
        if currentPos + 2 < len(c) and c[currentPos + 2] == 0:
            print("Jump 2")
            currentPos += 2
        else: 
            print("Jump 1")
            currentPos += 1
        jumpCount += 1
        print("Total jumps ", jumpCount)
    return jumpCount

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())
    n = 7
    arr = "0 0 1 0 0 1 0"
    # c = list(map(int, input().rstrip().split()))
    c = list(map(int, arr.rstrip().split()))

    result = jumpingOnClouds(c)
    print("Result is ", result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
