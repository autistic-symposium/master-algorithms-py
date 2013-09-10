#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

''' Example of how to use a bit array in python as a "counter" dict:

    >>> l1 = [0, 1, 2, 3, 4, 2, 6, 7, 8, 9]
    >>> print_dupl_ba(l1)
    2
'''



def print_dupl_ba(l1):
    bs = bytearray(10)
    for i in range(len(l1)):
        if i == l1[i]:
            bs[i] = 1
    for index, bit in enumerate(bs):
        if bit == 0:
            return l1[index]
    return None


    
    
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()

