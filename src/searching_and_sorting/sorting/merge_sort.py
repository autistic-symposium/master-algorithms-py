#!/usr/bin/python

__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"



''' Some examples of how to implement Merge Sort in Python.
    --> RUNTIME: WORST/BEST/AVERAGE Is O(nlogn)
    --> space complexity is O(n) for arrays
    --> in general not in place, good for large arrays
    --> In the case of two arrays: we can merge two arrays using the merge function from the merge sort
    --> we can do this for files too, merging each two

        1) If we can modify the arrays (pop) we can use:
            def merge(left, right):
                if not left or not right: return left or right # nothing to be merged
                result = []
                while left and right:
                    if left[-1] >= right[-1]:
                        result.append(left.pop())
                    else:
                        result.append(right.pop())
                result.reverse()
                return (left or right) + result


        2) If we can't modify or we want to in place, we need two pointers:
        >>> l1 = [1, 2, 3, 4, 5, 6, 7]
        >>> l2 = [2, 4, 5, 8]
        >>> merge(l1, l2)
        [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 8]


        3) For example, in the case we have a big array filled 0s in the end, and another array with the size of the number of 0s:
        >>> l1 = [1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0]
        >>> l2 = [2, 4, 5, 8]
        >>> merge_two_arrays_inplace(l1, l2)
        [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 8]


        4) If we want to merge sorted files (and we have plenty of RAM to load all files):
        >>> list_files = ['1.dat', '2.dat', '3.dat']
        >>> merge_files(list_files)
        [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8]
'''




"""
    The typical example...
"""

def merge_sort(seq):
    if len(seq) < 2:
        return seq
    mid = len(seq)//2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft)>1:
        lft = merge_sort(lft)
    if len(rgt)>1:
        rgt = merge_sort(rgt)

    res = []
    while lft and rgt:
        if lft [-1]>= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return(lft or rgt) + res




'''
    We could also divide this sort into two parts, separating
    the merge part in another function
'''

def merge_sort_sep(seq):
    if len(seq) < 2 :
        return seq    # base case
    mid = len(seq)//2
    left = merge_sort(seq[:mid])
    right = merge_sort(seq[mid:])   # notice that mid is included!
    return merge(left, right)      # merge iteratively



def merge(left, right):
    if not left or not right:
        return left or right # nothing to be merged
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if left[i:] : result.extend(left[i:])   # REMEMBER TO EXTEND, NOT APPEND
    if right[j:] : result.extend(right[j:])
    return result




''' The following merge functions is O(2n) and
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



''' Merge two arrays in place '''
def merge_two_arrays_inplace(l1, l2):
    if not l1 or not l2: return l1 or l2 # nothing to be merged
    p2 = len(l2) - 1
    p1 = len(l1) - len(l2) - 1
    p12 = len(l1) - 1
    while p2 >= 0 and p1 >= 0:
        item_to_be_merged = l2[p2]
        item_bigger_array = l1[p1]
        if item_to_be_merged < item_bigger_array:
            l1[p12] = item_bigger_array
            p1 -= 1
        else:
            l1[p12] = item_to_be_merged
            p2 -= 1
        p12 -= 1
    return l1



''' Merge sort for files '''
def merge_files(list_files):
    result = []
    final = []
    for filename in list_files:
        aux = []
        with open(filename, 'r') as file:
            for line in file:
                aux.append(int(line))
        result.append(aux)
    final.extend(result.pop())
    for l in result:
        final = merge(l, final)
    return final





def test_merge_sort():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    seq_sorted = sorted(seq)
    assert(merge_sort(seq) == seq_sorted)
    assert(merge_sort_sep(seq) == seq_sorted)
    print('Tests passed!')


if __name__ == '__main__':
    test_merge_sort()
