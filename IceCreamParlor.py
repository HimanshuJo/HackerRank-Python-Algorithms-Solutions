# https://www.hackerrank.com/challenges/icecream-parlor/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
  res=[]
  sizeOfArr=len(arr)
  for i in range(0, sizeOfArr, 1):
    currElementAtIndexI=arr[i]
    haveFoundPairOrNot=False
    for j in range(0, sizeOfArr, 1):
      if i!=j:
        otherPairMemberNeededToBeFound=m-currElementAtIndexI;
        if arr[j]==otherPairMemberNeededToBeFound:
          res.append(i+1)
          res.append(j+1)
          haveFoundPairOrNot=True
          res.sort()
          break
    if haveFoundPairOrNot==True:
      break
  return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
