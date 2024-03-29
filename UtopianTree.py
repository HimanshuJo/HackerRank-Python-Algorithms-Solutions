# https://www.hackerrank.com/challenges/utopian-tree/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    if n==0:
        return 1
    res=1
    count=0
    while(1):
        if n==0:
            break
        if count%2==0:
            res*=2
        else:
            res+=1
        count+=1
        n-=1
    return res
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
