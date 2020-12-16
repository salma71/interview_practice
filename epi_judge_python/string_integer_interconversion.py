from test_framework import generic_test
from test_framework.test_failure import TestFailure

import functools
import string

def int_to_string(x: int) -> str:
    # set a flag to reserve the int sign
    negative = False
    # if x is less than zero, negate the flag and append to x
    if x < 0:
        x, negative = -x, True

    # create an empty list to store the new number
    str_arr = []
    #while the flag is true iterate over the input number
    while True:
        # initialize the partial result to zero
        r = ord('0')
        #get the LSD using mod and put it at the begining of the array
        lsd = x % 10
        # appenf the lsd and r in s
        str_arr.append(chr(r + lsd))
        # set x to the remaining number (slice by one digit)
        x //= 10
        #stop when x = 0 
        if x == 0:
            break
        
    # return the reversed number after appending the negative sign into it
    return('-' if negative else '') + ''.join(reversed(str_arr))
    
        
        

def string_to_int(s: str) -> int:
    return (-1 if s[0] == '-' else 1) * functools.reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.index(c),
        s[s[0] in '-+':], 0)


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
