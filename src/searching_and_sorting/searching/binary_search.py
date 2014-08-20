#!/usr/bin/python

__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"



def binary_search(seq, key):
    ''' binary search iterative algorithm '''
    ''' observe that the index is returned '''
    hi = len(seq)
    lo = 0
    while lo < hi:
        mid = (hi+lo) // 2
        if seq[mid] == key:
            return mid
        elif key < seq[mid]:
            hi = mid
        else:
            lo = mid + 1


def binary_search_rec(seq, key, lo=0, hi=None):
    ''' binary search recursive algorithm '''
    hi = hi or len(seq)
    if hi < lo: return None
    mid = (hi + lo) // 2
    if seq[mid] == key:
        return mid
    elif seq[mid] < key:
        return binary_search_rec(seq, key, mid + 1, hi)
    else:
        return binary_search_rec(seq, key, lo, mid - 1)


def test_binary_search():
    seq = [1,2,5,6,7,10,12,12,14,15]
    key = 6
    assert(binary_search(seq, key) == 3)
    assert(binary_search_rec(seq, key) == 3)
    print('Tests passed!')


if __name__ == '__main__':
    test_binary_search()




