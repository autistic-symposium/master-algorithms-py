#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

''' Given two 32-bit numbers, N and M, and two bit positions, i and j, this
    method insert M into N such that M starts at bit j and ends at bit i: 
    1) clear the bits j thru i in N'
    2) shift M so that it lines up with bits j thru i
    3) merge M and N

    >>> N = 0b10000000000
    >>> M = 0b10011
    >>> j = 6
    >>> i = 2
    >>> insert_small_bin_into_big_bin(M, N, i, j)
    '0b10001001100'
'''

def insert_small_bin_into_big_bin(M, N, i, j):
    allOnes = ~0
    left = allOnes << (j+1) # 1110000
    right = ( (1 << i) - 1) # 0000111
    mask = left | right     # 1110111
    N_cleared = N & mask
    M_shifted = M << i
    
    return bin( N_cleared | M_shifted)
    
  
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()

