#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    countpos=0
    countnegs=0
    countzeros=0
    sz=len(arr)
    for vals in arr:
        if vals>0:
            countpos+=1
        elif vals<0:
            countnegs+=1
        elif vals==0:
            countzeros+=1
    print("%.6f\n%.6f\n%.6f" %(countpos/sz, countnegs/sz, countzeros/sz))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
