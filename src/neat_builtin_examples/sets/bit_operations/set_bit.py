#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

''' Set a bit in a binary number:
    1) Shifts 1 over by i bits
    2) make an OR with the number, only the value at bit i will change and all the others bit
    of the mask are zero so will not affect the num
    >>> num = int('0100100', 2)
    >>> set_bit(num, 0)   
    '0b100101'
    >>> set_bit(num, 1)   
    '0b100110'
    >>> set_bit(num, 2)    # nothing change
    '0b100100'
    >>> set_bit(num, 3)   
    '0b101100'
    >>> set_bit(num, 4)   
    '0b110100'
    >>> set_bit(num, 5)     # nothing change
    '0b100100'
'''



def set_bit(num, i):
    mask = 1 << i
    return bin( num | mask ) 


    
    
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()

