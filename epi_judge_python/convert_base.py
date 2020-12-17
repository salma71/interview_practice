from test_framework import generic_test
import functools
import string


def convert_base(num_as_string: str, b1: int, b2: int) -> str:

    # create a function to change the created integer into b2 base
    def construct_from_base(num_as_int, b2):
        return('' if num_as_int == 0 else
               construct_from_base(num_as_int // b2, b2) +
               string.hexdigits[num_as_int % b2].upper())

    # check the sign of the num_as_string is negative
    is_negative = num_as_string[0] == '-'
    # convert num_as_str to decimal of base b1
    num_as_int = functools.reduce(
        lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
        num_as_string[is_negative:], 0
    )
    return ('-' if is_negative else '') + ('0' if num_as_int == 0 else
                                           construct_from_base(num_as_int, b2))



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
