#!/usr/bin/python

__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"

import random

def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp


def qselect(A, k, left=None, right=None):
    left = left or 0
    right = right or len(A) - 1
    pivot = random.randint(left, right)
    pivotVal = A[pivot]

    # Move pivot out of the sorting range
    swap(A, pivot, right)
    swapIndex, i = left, left
    while i <= right - 1:
        if A[i] < pivotVal:
            swap(A, i, swapIndex)
            swapIndex += 1
        i += 1

    # Move pivot to final position
    swap(A, right, swapIndex)

    # Check if pivot matches, else recurse on the correct half
    rank = len(A) - swapIndex
    if k == rank:
        return A[swapIndex]
    elif k < rank:
        return qselect(A, k, left=swapIndex+1, right=right)
    else:
        return qselect(A, k, left=left, right=swapIndex-1)



def find_k_largest_seq_quickselect(seq, k):
    ''' perform quick select to get kth element, and find all elements larger '''
    kth_largest = qselect(seq, k)
    result = []
    for item in seq:
        if item >= kth_largest:
            result.append(item)
    return result



def test_find_k_largest_seq_quickselect():
    seq = [3, 10, 4, 5, 1, 8, 9, 11, 5]
    k = 2
    assert(find_k_largest_seq_quickselect(seq,k) == [10, 11])
    print("Tests passed!")


if __name__ == '__main__':
    test_find_k_largest_seq_quickselect()

