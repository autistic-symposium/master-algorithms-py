#!/usr/bin/env python

__author__ = "bt3"


def qs(array):
    '''
    >>> qs([4,1,6,2,7,9,3])
    [1, 2, 3, 4, 6, 7, 9]
    '''
    if len(array) < 2:
        return array

    piv = len(array)//2
    piv_element = array[piv]
    new_array = array[:piv] + array[piv+1:]

    left  = [a for a in new_array if a <= piv_element]
    right = [a for a in new_array if a > piv_element]


    return qs(left) + [array[piv]] + qs(right)


if __name__ == '__main__':
    import doctest
    doctest.testmod()