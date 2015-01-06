#!/bin/python


def binary_search_rec(array, item, lo=0, hi = None):
    '''
    >>> binary_search_rec([2,3,5,6,8,10,15,23], 15)
    (True, 6)
    >>> binary_search_rec([2,3,5,6,8,10,15,23], 4)
    False
    '''
    hi = hi or len(array)
    if hi < lo :
        return False

    mid = (hi + lo)//2

    if array[mid] == item:
        return True, mid
    elif array[mid] < item:
        return binary_search_rec(array, item, mid + 1, hi)
    else:
        return binary_search_rec(array[:mid], item, lo, mid -1)



def binary_search_iter(array, item):
    '''
    >>> binary_search_iter([2,3,5,6,8,10,15,23], 15)
    (True, 6)
    >>> binary_search_iter([2,3,5,6,8,10,15,23], 4)
    False
    '''
    hi = len(array)
    lo = 0

    while lo < hi:
        mid = (hi+lo)//2
        if array[mid] == item:
            return True, mid
        elif array[mid] > item:
            hi = mid
        else:
            lo  = mid + 1
    return False





if __name__ == '__main__':
    import doctest
    doctest.testmod()

