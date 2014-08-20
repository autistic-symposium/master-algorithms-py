#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

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

''' This is the main function that keep dividing the seq '''
def merge_sort(seq):
    if len(seq) < 2 : return seq    # base case
    mid = len(seq)//2
    left, right = None, None            # we could have declared the arrays here, 
                                        # but this would allocate unecessary extra space   
    if seq[:mid]: left = merge_sort(seq[:mid])
    if seq[mid:]: right = merge_sort(seq[mid:])   # notice that mid is included!
    
    return merge(left, right)      # merge iteratively


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
    
    
   



if __name__ == '__main__':
    import doctest
    doctest.testmod()


