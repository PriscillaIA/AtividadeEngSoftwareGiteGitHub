#!/bin/python3

import math
import os
import random
import re
import sys

# This function return the sum of all elements in the array
def sum_elements_of_array(ar):
    return sum(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sum_elements_of_array(ar)

    fptr.write(str(result) + '\n')

    fptr.close()