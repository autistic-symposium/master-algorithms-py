#!/usr/bin/env python

__author__ = "bt3"


def merge_sort(seq):
    '''
    >>> seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    >>> merge_sort(seq)
    [0, 1, 2, 2, 3, 3, 5, 5, 6, 6, 8]
    '''
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



# separating the merge part in another function
def merge_sort_sep(seq):
    '''
    >>> seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    >>> merge_sort_sep(seq)
    [0, 1, 2, 2, 3, 3, 5, 5, 6, 6, 8]
    '''
    if len(seq) < 2 :
        return seq
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


if __name__ == '__main__':
    import doctest
    doctest.testmod()