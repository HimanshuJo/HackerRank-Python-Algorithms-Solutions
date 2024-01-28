# https://www.hackerrank.com/challenges/birthday-cake-candles/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    maxx=-sys.maxsize - 1
    sz=len(candles)
    mp={}
    for vals in candles:
        maxx=max(maxx, vals)
        if vals in mp:
            mp[vals]=mp[vals]+1
        else:
            mp[vals]=1
    return mp[maxx]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
