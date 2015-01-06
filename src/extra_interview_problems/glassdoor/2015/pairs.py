#!/bin/python

'''
Given an unsorted array of numbers (that may contain repeated numbers),
 * data structure that contains all the pairs w/sum equal to  k.
 * Do not include pairs that are the same numbers in a different order.
'''

from collections import Counter

def sum_pairs(array, k):
    '''
    >>> sum_pairs([1, 4, 2, 7, 1, 3, 10, 15, 3, 1], 6)
    set([(3, 3)])
    >>> sum_pairs([1, 4, 2, 7, 1, 3, 10, 15, 3, 1], 0)
    set([])
    '''

    results = set()
    dict = Counter()

    for i in array:
        dict[i] += 1

    for i in array:
        if dict[k-i] > 0:
            if i == k-i and dict[k-i] > 1:
                    results.add((i, k-i))
                    dict[k-i] -= 2
            elif i == k-i:
                results.add((i, k-i))
                dict[k-i] -= 1


    return results


if __name__ == '__main__':
    import doctest
    doctest.testmod()

