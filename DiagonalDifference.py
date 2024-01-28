# https://www.hackerrank.com/challenges/diagonal-difference/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    rws=len(arr)
    cols=len(arr[0])
    rwsm=0
    colssm=0
    j=cols-1
    for index, _ in enumerate(arr):
        rwsm+=arr[index][index]
        colssm+=arr[index][j]
        j-=1
    return abs(rwsm-colssm)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
