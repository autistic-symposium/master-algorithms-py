#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

''' Given a sorted array that was rotated, find an item with binary search:
    >>> l1 = [3, 4, 5, 6, 7, 1, 2]
    >>> find_element_rot_array(l1, 7)
    4
    >>> find_element_rot_array(l1, 3)
    0
    >>> find_element_rot_array(l1, 4)
    1
    >>> find_element_rot_array(l1, 5)
    2
    >>> find_element_rot_array(l1, 6)
    3
    >>> find_element_rot_array(l1, 1)
    5
    >>> find_element_rot_array(l1, 2)
    6
    >>> find_element_rot_array(l1, 8)   
    
'''

def find_element_rot_array(seq, key, lo=0, hi=None):
    hi = hi or len(seq)
    if hi <= lo: return None # base case: <= for odd and even numbers!
    mid = (hi + lo) // 2    
    if key == seq[mid]: return mid
    
    # if left is ordered --> we work here
    if seq[lo] <= seq[mid]:
        # now, is the key there?
        if key < seq[mid] and key >= seq[lo]:
            return find_element_rot_array(seq, key, lo, mid)
        else:
        # all the other cases
            return find_element_rot_array(seq, key, mid+1, hi)
    
    # right is ordered --> we work here
    else:
        # now, is the key there?
        if key > seq[mid] and key <= seq[hi-1]: # stupid hi-1!!!
            return find_element_rot_array(seq, key, mid+1, hi)
        else:
        # all the other cases
            return find_element_rot_array(seq, key, lo, mid)

    
    
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()

