from test_framework import generic_test
import functools

def ss_decode_col_id(col: str) -> int:
    
    return(functools.reduce(
        lambda res, c: res * 26 + ord(c) - ord('A') + 1, col, 0
    ))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
