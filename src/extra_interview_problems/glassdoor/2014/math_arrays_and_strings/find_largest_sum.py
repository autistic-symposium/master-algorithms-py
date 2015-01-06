#!/usr/bin/env python

__author__ = "bt3"



'''You are given an array of integers (both positive and negative). Find the contiguous
sequence with the largest sum. Return the sum.'''


def find_largest_sum(array):
    '''
    >>> find_largest_sum([-1, 2, -3, 5, 3, 1, -16, 7, 1, -13, 1])
    9
    >>> find_largest_sum([])
    0
    >>> find_largest_sum([1])
    1
    '''
    if not array: return 0
    p1, p2 = 0, 1
    all_sums = set()
    sum_ = array[p1]

    while p1 < p2 and p2 < len(array):
        if sum_ + array[p2] < 0:
            all_sums.add(sum_)
            p2 += 1
            p1 = p2
            sum_ = 0
        sum_ += array[p2]
        p2 += 1
    all_sums.add(sum_)
    return max(all_sums)



def find_largest_sum_simple(array):
    '''
    >>> find_largest_sum_simple([-1, 2, -3, 5, 3, 1, -16, 7, 1, -13, 1])
    9
    >>> find_largest_sum_simple([])
    0
    >>> find_largest_sum_simple([1])
    1
    '''
    max_sum, sum_ = 0, 0

    for item in array:
        sum_ += item
        if max_sum < sum_:
            max_sum = sum_
        elif sum_ < 0:
            sum_ = 0
    return max_sum




if __name__ == '__main__':
    import doctest
    doctest.testmod()