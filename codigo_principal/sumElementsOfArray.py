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

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sum_elements_of_array(ar)

    with open(os.environ['OUTPUT_PATH'], 'w') as fptr: 
        fptr.write(str(result) + '\n')


