#!/usr/bin/env python

__author__ = "bt3"

''' find the longest continuous increasing subsequence'''


def find_long_con_inc(seq):
    '''
    >>> find_long_con_inc([1, -2, 3, 5, 1, -1, 4, -1, 6])
    [-2, 3, 5]
    >>> find_long_con_inc([1, 3, -2, 3, 5, 6])
    [-2, 3, 5, 6]
    '''

    aux = []
    result = []
    seq.append(-float('infinity'))

    for i, pivot in enumerate(seq[:-1]):
        aux.append(pivot)
        if pivot > seq[i+1]:
            if len(aux) > len(result):
                result = aux
            aux = []

    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
