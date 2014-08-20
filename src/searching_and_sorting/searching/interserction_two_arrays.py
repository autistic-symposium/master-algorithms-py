#!/usr/bin/python

__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"



''' using sets '''

def intersection_two_arrays_sets(seq1, seq2):
    ''' find the intersection of two arrays using set proprieties '''
    set1 = set(seq1)
    set2 = set(seq2)
    return set1.intersection(set2)  #same as list(set1 & set2



''' using merge sort '''

def intersection_two_arrays_ms(seq1, seq2):
    ''' find the intersection of two arrays using merge sort '''
    res = []
    while seq1 and seq2:
        if seq1[-1] == seq2[-1]:
            res.append(seq1.pop())
            seq2.pop()
        elif seq1[-1] > seq2[-1]:
            seq1.pop()
        else:
            seq2.pop()
    res.reverse()
    return res




''' using binary search '''

def binary_search(seq, key, lo=0, hi=None):
    ''' binary search iterative algorithm '''
    hi = hi or len(seq)
    while lo < hi:
        mid = (hi+lo) // 2
        if seq[mid] == key:
            return True
        elif key > seq[mid]:
            lo = mid + 1
        else:
            hi = mid
    return None

def intersection_two_arrays_bs(seq1, seq2):
    ''' if A small and B is too large, we can do a binary search on each entry in B '''
    ''' only works if sorted and the small sequence has not larger nmbers!!!'''
    if len(seq1) > len(seq2): seq, key = seq1, seq2
    else: seq, key = seq2, seq1

    intersec = []
    for item in key:
        if binary_search(seq, item):
            intersec.append(item)
    return intersec



def test_intersection_two_arrays(module_name='this module'):
    seq1 = [1,2,3,5,7,8]
    seq2 = [3,5,6]

    assert(set(intersection_two_arrays_sets(seq1,seq2)) == set([3,5]))
    assert(intersection_two_arrays_bs(seq1,seq2) == [3,5])
    assert(intersection_two_arrays_ms(seq1,seq2) == [3,5])

    s = 'Tests in {name} have {con}!'
    print(s.format(name=module_name, con='passed'))


if __name__ == '__main__':
    test_intersection_two_arrays()

