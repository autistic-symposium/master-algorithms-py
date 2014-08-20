#!/usr/bin/python

__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"


''' Some examples of how to implement Merge Sort in Python
    --> RUNTIME: WORST/BEST/AVERAGE Is O(nlogn)
    --> space complexity is O(n) for arrays
    --> not in place, good for large arrays
    >>> seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    >>> merge_sort(seq) == sorted(seq)
    True
    >>> seq2 = [3, 3, 3, 3, 3, 3, 3, 3]
    >>> merge_sort(seq2) == sorted(seq2)
    True
    >>> seq3 = []
    >>> merge_sort(seq3) == sorted(seq3)
    True
'''


def merge_sort(seq):
    if len(seq) <= 1: return seq
    mid = len(seq)//2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft)>1: lft = merge_sort(lft)
    if len(rgt)>1: rgt = merge_sort(rgt)

    res = []
    while lft and rgt:
        if lft [-1]>= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return(lft or rgt) + res



def test_merge_sort():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    assert(merge_sort(seq) == sorted(seq))
    print('Tests passed!')


'''
    We could also divide this sort into two parts, separating
    the merge part in another function
'''

def merge_sort_sep(seq):
    if len(seq) < 2 : return seq    # base case
    mid = len(seq)//2
    left, right = None, None            # we could have declared the arrays here,
                                        # but this would allocate unecessary extra space
    if seq[:mid]: left = merge_sort(seq[:mid])
    if seq[mid:]: right = merge_sort(seq[mid:])   # notice that mid is included!

    return merge(left, right)      # merge iteratively

def merge(left, right):
    if not left or not right: return left or right # nothing to be merged
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if left[i:] : result.extend(left[i:])   # REMEMBER TO TO ENXTEND NOT APPEND
    if right[j:] : result.extend(right[j:])
    return result




''' The two following merge functions are O(2n)=O(n) and O(n) respectively. They
    illustrate many features in Python that '''
def merge_2n(left, right):
    if not left or not right: return left or right # nothing to be merged
    result = []
    while left and right:
        if left[-1] >= right[-1]:
            result.append(left.pop())
        else:
            result.append(right.pop())
    result.reverse()
    return (left or right) + result







if __name__ == '__main__':
    test_merge_sort()
