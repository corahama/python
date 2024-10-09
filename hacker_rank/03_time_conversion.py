#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    match = re.search('(\d\d)(:\d\d:\d\d)(\D\D)', s)
    hours = int(match.group(1))
    if match.group(3) == 'PM':
        return f'{hours if hours == 12 else hours+12}{match.group(2)}'
    else:
        return f'{"00" if hours == 12 else str(hours).zfill(2)}{match.group(2)}'

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result)
