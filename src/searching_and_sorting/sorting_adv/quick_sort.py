#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail


''' Some examples of how to implement Quick Sort in Python 
    --> RUNTIME: BEST/AVERAGE Is O(nlogn), WORST is O(n2)
    --> the first example is not in place, the second is in place
    --> test with two element arrays, identical values
    
    Quick sort in place:
    1) select pivot as the index = 0
    2) start pointer1 at index = 1 and pointer2 in the last element
    3) while pointer1 < pointer2:
        if value in pointer1 <= pivot
            swap value in pointer1 with value in pointer2 and advanced pointer2
        else
            advance pointer1
    4) now the array is like this:
        [pivot, larger than pivot, smaller than pivot]
    5) swap the pivot where pointer 1 stop
    6) do recursively for [smaller] + [pivot] + [larger]
    
    >>> seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    >>> quick_sort(seq) == sorted(seq)
    True
    >>> quick_sort([3, 3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3, 3]
    True
    >>> quick_sort([]) == []
    True
    >>> quick_sort([2,1]) == [1, 2]
    True
    >>> quick_sort_in(seq) == sorted(seq)
    True
    >>> quick_sort_in([3, 3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3, 3]
    True
    >>> quick_sort_in([]) == []
    True
    >>> quick_sort_in([2,1]) == [1, 2]
    True
'''

def quick_sort(seq):
    if len(seq) < 2 : return seq    
    mid = len(seq)//2
    pi = seq[mid]
    seq = seq[:mid] + seq[mid+1:]  
    left = quick_sort([x for x in seq if x <= pi])    # REMEMBER TO INCLUDE X  (OR IN RIGHT)
    right = quick_sort([x for x in seq if x > pi])   
    return left + [pi] + right
    



def quick_sort_in(seq): 
    if len(seq) < 2 : return seq 
    if len(seq) == 2 and seq[0] > seq[1]:
        seq[0], seq[1] = seq[1], seq[0]   # problems when only 2 elements because of swap
    pivot = seq[0]  # start at the ends because we don't know how many elements
    p1, p2 = 1, len(seq) -1   # set pointers at both ends
    while p1 < p2: # must be < or out of range
        if seq[p1] <= pivot: # must be <= because of pivot swap
                seq[p1], seq[p2] = seq[p2], seq[p1]
                p2 -= 1
        else:
            p1 += 1
    seq[0], seq[p1] = seq[p1], pivot 
    return quick_sort_in(seq[p1+1:]) + [seq[p1]] + quick_sort_in(seq[:p1])



if __name__ == '__main__':
    import doctest
    doctest.testmod()
