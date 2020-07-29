#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0
    for i in range(len(q)-1,-1,-1):
        if q[i] - (i + 1) > 2:
            print('Too chaotic in q[i] = ', q[i])
            bribes = 'Too chaotic'
            break
        for j in range(max(0, q[i] - 2),i):
            if q[j] > q[i]:
                print("sum bribe of q[j] = ", q[j], ", and q[i] = ", q[i])
                bribes+=1
    return bribes

if __name__ == '__main__':
    # t = int(input())
    t = 2
    # ns = [5, 5]
    # qs = ["2 1 5 3 4", "2 5 1 3 4"]

    ns = [8, 8]
    qs = ["5 1 2 3 7 8 6 4", "1 2 5 3 7 8 6 4"]
    
    for t_itr in range(t):
        # n = int(input())
        n = ns[t_itr]

        # q = list(map(int, input().rstrip().split()))
        q = list(map(int, qs[t_itr].rstrip().split()))

        result = minimumBribes(q)
        print(result)
