#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

''' A recursive and an iterative example of binary search in Python.
    Remember: sequence must be sorted! You can return True/False or the index:
    >>> l1 = [1, 2, 3, 4, 5, 6, 7]
    >>> binary_search_rec(l1, 1)
    0
    >>> binary_search_rec(l1, 2)
    1
    >>> binary_search_rec(l1, 3)
    2
    >>> binary_search_rec(l1, 4)
    3
    >>> binary_search_rec(l1, 5)
    4
    >>> binary_search_rec(l1, 6)
    5
    >>> binary_search_rec(l1, 7)         
    6
    >>> binary_search_rec(l1, 8)       
    >>> l1 = [1, 2, 3, 4, 5, 6]
    >>> binary_search_rec(l1, 1)
    0
    >>> binary_search_rec(l1, 2)
    1
    >>> binary_search_rec(l1, 3)
    2
    >>> binary_search_rec(l1, 4)
    3
    >>> binary_search_rec(l1, 5)
    4
    >>> binary_search_rec(l1, 6)
    5
    >>> binary_search_rec(l1, 7) 
    >>> l1 = [1, 2, 3, 4, 5, 6, 7]
    >>> binary_search_iter(l1, 1)
    0
    >>> binary_search_iter(l1, 2)
    1
    >>> binary_search_iter(l1, 3)
    2
    >>> binary_search_iter(l1, 4)
    3
    >>> binary_search_iter(l1, 5)
    4
    >>> binary_search_iter(l1, 6)
    5
    >>> binary_search_iter(l1, 7)         
    6
    >>> binary_search_iter(l1, 8)       
    >>> l1 = [1, 2, 3, 4, 5, 6]
    >>> binary_search_iter(l1, 1)
    0
    >>> binary_search_iter(l1, 2)
    1
    >>> binary_search_iter(l1, 3)
    2
    >>> binary_search_iter(l1, 4)
    3
    >>> binary_search_iter(l1, 5)
    4
    >>> binary_search_iter(l1, 6)
    5
    >>> binary_search_iter(l1, 7)      
'''
    

def binary_search_iter(seq, key):
    hi, lo = len(seq), 0      
    while lo < hi: # here is <!
        mid = (hi+lo)//2
        if key == seq[mid]: return mid
        elif key < seq[mid]: hi = mid 
        else: lo = mid + 1
    return None


def bool_binary_search_iter(seq, key):
    hi, lo = len(seq), 0      
    while lo < hi:
        mid = (hi+lo)//2
        if key == seq[mid]: return True
        elif key < seq[mid]: hi = mid 
        else: lo = mid + 1
    return False


def binary_search_rec(seq, key, lo=0, hi=None):
    hi = hi or len(seq)
    if hi <= lo: return None # base case: <= for odd and even numbers!
    mid = (hi + lo) // 2    
    if key == seq[mid]: return mid
    elif key < seq[mid] : return binary_search_rec(seq, key, lo, mid) # include until mid-1
    else: return binary_search_rec(seq, key, mid+1, hi)   


def bool_binary_search_rec(seq, key, lo=0, hi=None):
    hi = hi or len(seq)
    if hi <= lo: return False # base case: <= for odd and even numbers!
    mid = (hi + lo) // 2    
    if key == seq[mid]: return True
    elif key < seq[mid] : return bool_binary_search_rec(seq, key, lo, mid) 
    else: return bool_binary_search_rec(seq, key, mid+1, hi)   


    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
