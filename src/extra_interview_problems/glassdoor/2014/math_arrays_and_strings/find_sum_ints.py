#!/usr/bin/env python

__author__ = "bt3"



from collections import defaultdict

def find_ints_sum(array, sum_):
    '''
    >>> find_ints_sum([4, 5, 3, 5, 2, 8, 1], 9)
    set([(5, 4), (1, 8)])
    >>> find_ints_sum([1, 2], 5)
    set([])
    >>> find_ints_sum([1], 1)
    'Not enough values'
    '''
    if len(array)< 2:
        return "Not enough values"

    dict = defaultdict()
    pairs = set()

    for i in array:
        if (sum_ - i) in dict:
            pairs.add((i, sum_ -i))
        else:
            dict[i] = True

    return pairs

# if the array was sorted, we could do this with two pointers

if __name__ == '__main__':
    import doctest
    doctest.testmod()