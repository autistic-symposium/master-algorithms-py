#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

''' Find how many bits a int has:
    1) Start with a mask of 1
    2) Mask with AND
    3) if result (if true): count += 1
    (obs: to find the int of a bin do int('1001', 2)) and to show in bin do bin(int))
    
    >>> for i in range(17): print(find_bit_len(i))
'''



def find_bit_len(int_num):
    lenght = 0
    while int_num:
        int_num >>= 1
        lenght += 1
    return lenght
    
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()

