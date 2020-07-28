#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedStringOld(s, n):
    rep = math.ceil(n/len(s))
    extendedS = (s*rep)[0:n]
    print("extendedS = ", extendedS)
    repeatedAs = len(re.sub('[^a]','', extendedS))
    return repeatedAs

def repeatedString(s, n):
    a_count_single = len(re.sub('[^a]','', s))
    rep = math.floor(n/len(s))
    a_count = a_count_single*rep
    
    still_need = n - (rep*len(s))
    
    rem_s = s[0:still_need]
    a_count += len(re.sub('[^a]','', rem_s))
    
    print("still need = ", still_need)
    print("a_count = ", a_count)

    return a_count

if __name__ == '__main__':
    s = "aba"

    n = 10

    result = repeatedString(s, n)
    print("Result is ", result)

