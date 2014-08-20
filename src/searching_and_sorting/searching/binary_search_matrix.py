#!/usr/bin/python

__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"


''' Searches an element in a matrix where in every row, the values are increasing from left to right, but the last number in a row is smaller than the first number in the next row.

    (1) The naive brute force solution (sequential search)  scan all numbers and cost O(nm).  However, since the numbers are already sorted, the matrix can be viewed as a 1D sorted array.  The binary search algorithm is suitable. The efficiency is O(logmn).

    >>> m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> binary_search_matrix_rec(m, 6)
    (1, 2)
    >>> binary_search_matrix_rec(m, 12)
    >>> binary_search_matrix_iter(m, 6)
    (1, 2)
    >>> binary_search_matrix_iter(m, 12)
    >>> binary_search_matrix_iter(m, 1)
    (0, 0)

    (2) Another solution is "discarding" arrays in the way. The efficiency is O(logm).
    >>> m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> searching_matrix(m, 6)
    (1, 2)
    >>> searching_matrix(m, 12)

'''


def binary_search_matrix_rec(m, key, lo=0, hi=None):
    if not m: return None
    rows = len(m)
    cols = len(m[0])
    hi = hi or rows*cols
    if hi > lo: # -----> REMEMBER THIS OR INDEX WILL EXPLODE!!!!!!!!
        mid = (hi + lo)//2
        row = mid//cols
        col = mid%cols
        item = m[row][col]
        if key == item: return row, col
        elif key < item: return binary_search_matrix_rec(m, key, lo, mid-1)
        else: return binary_search_matrix_rec(m, key, mid+1, hi)
    return None



def binary_search_matrix_iter(m, key):
    if not m: return None
    rows = len(m)
    cols = len(m[0])
    lo, hi = 0, rows*cols
    while lo < hi:
        mid = (hi + lo)//2
        row = mid//rows
        col = mid%rows
        item = m[row][col]
        if key == item: return (row, col)
        elif key < item: hi = mid
        else: lo = mid +1
    return None


def searching_matrix(m, key):
    if not m: return None
    rows = len(m)
    cols = len(m[0])
    i, j = 0, cols -1
    while i < rows and j > 0:
        item = m[i][j]
        if key == item: return (i, j)
        elif key < item: j -= 1
        else: i += 1
    return None


if __name__ == '__main__':
    import doctest
    doctest.testmod()
