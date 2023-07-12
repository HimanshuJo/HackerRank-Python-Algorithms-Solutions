#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    vec=[[' ' for y in range(n)] for x in range(n)]
    for i in range(n):
        count=i+1
        for j in reversed(range(n)):
            if count==0:
                break
            vec[i][j]='#'
            count-=1
    for i in range(n):
        s=''.join(str(x) for x in vec[i])
        print(s)

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
