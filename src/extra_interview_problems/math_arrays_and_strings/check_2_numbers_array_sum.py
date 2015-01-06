#!/usr/bin/env python

__author__ = "bt3"

"""
Given an integer x and an unsorted array of integers, describe an
algorithm to determine whether two of the numbers add up to x.

1. Using hash tables.
2. Sorting the array and keeping two pointers in the array, one in
the beginning and one in the end. Whenever the sum of the current
two integers is less than x, move the first pointer forwards, and
whenever the sum is greater than x, move the second pointer
backwards. O(nln n).
3. Create a BST with x minus each element in the array.
Check whether any element of the array appears in the BST.
It takes O(nlog n) times two.
"""

def check_sum_hash_table(array, k):
    '''
    >>> check_sum_hash_table([3, 2, 6, 7, 9, 1], 8)
    [(6, 2), (1, 7)]
    >>> check_sum_hash_table([5, 2, 6, 7, 9, 1], 4)
    []
    >>>
    '''

    from collections import defaultdict

    dict = defaultdict()
    res = []

    for i in array:
        if k-i in dict:
            res.append((i, k-i))
            del dict[k-i]
        else:
            dict[i] = 1

    return res

if __name__ == '__main__':
    import doctest
    doctest.testmod()