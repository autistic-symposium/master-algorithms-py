#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

''' Given a sorted an array with empty strings, we use binary search to find some string (since
    the list is sorted):
    --> we deal with the empty strings with strip and then run to left and right, or move
    mid to the closed non-empty str (remember that the index must be conserved):
    >>> l1 = ['acre', 'ball', '', 'coach', '', 'cut', '']
    >>> find_str_array_with_empty_str(l1, l1[0])
    0
    >>> find_str_array_with_empty_str(l1, l1[1])
    1
    >>> find_str_array_with_empty_str(l1, l1[3])
    3
    >>> find_str_array_with_empty_str(l1, l1[5])
    5
    >>> find_str_array_with_empty_str(l1, 'bla')
'''


def find_str_array_with_empty_str(seq, s1):
    if not seq or not s1: return None
    hi = len(seq)
    lo = 0
    while hi > lo:
        mid = (hi+lo)//2
        
        if seq[mid] == '':
            while True:
                left = mid-1
                right = mid+1
                if left < lo or right > hi: return None
                elif right < hi and seq[right]: 
                    mid = right
                    break
                elif left > lo and seq[left]: 
                    mid = left
                    break
                right += 1
                left -= 1
       
        if s1 == seq[mid] == s1: return mid
        elif s1 < seq[mid]: hi = mid 
        else: lo = mid + 1
    
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()

