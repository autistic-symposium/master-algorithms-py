#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

''' Swap odd and even bits in a smart way in a binary:
    1) first for odds, take n and move the odd:
        (a) Mask all odd bits with 10101010 (0xAA)
        (b) shift by right by 1
    2) do the same to ints with 01010101
    3) merge
    
    >>> num = 0b11011101
    >>> result = '0b1101110'
    >>> swap_odd_even(num) == result
    True

'''



def swap_odd_even(num):
    mask_odd = 0xAA # 0b10101010
    mask_even = 0x55 # 0b1010101
    odd = num & mask_odd
    odd >>= 1
    even = num & mask_even
    even >>= 1
    return bin(odd | even)


    
    
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()

