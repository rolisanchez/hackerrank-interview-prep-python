#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulationSlow(n, queries):
    array = [0]*n
    print("array = ", array)
    for query in queries:
        left = query[0]
        right = query[1]
        add = query[2]
        array[left-1:right] = list(map(lambda x: x + add, array[left-1:right]))
        print("array = ", array)

    return max(array)

def arrayManipulation(n, queries):
    array = [0]*(n+1)
    for query in queries:
        print("array ", array)
        a = query[0]
        b = query[1]
        k = query[2]
        array[a-1] += k
        array[b] -= k

    answer = 0
    current = 0

    for x in array:
        current += x
        answer = max(answer, current)
    return answer

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nm = input().split()

    # n = int(nm[0])

    # m = int(nm[1])
    n = 5

    m = 3
    arr = ["1 2 100", "2 5 100", "3 4 100"]

    queries = []

    for i in range(m):
        # queries.append(list(map(int, input().rstrip().split())))
        queries.append(list(map(int, arr[i].rstrip().split())))

    result = arrayManipulation(n, queries)
    print("Result is = ", result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
