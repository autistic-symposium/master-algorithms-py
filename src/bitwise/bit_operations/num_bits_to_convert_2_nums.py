#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

''' This method returns the number of bits that are necessary to change to convert two
    numbers A and B:
    1) XOR
    2) count 1s
        
    >>> a = int('10010000', 2)
    >>> b = int('01011010', 2)
    >>> count_bits_swap(a, b)  
    4
    >>> count_bits_swap2(a, b)  
    4
'''

def count_bits_swap2(a, b):
    count = 0
    m = a^b
    while m:
        count +=1
        m = m & (m-1)
    return count



def count_bits_swap(a, b):
    m = a^b
    return count_1s(m)
    
    
def count_1s(m):
    count = 0
    while m:
        if m& 1 :
            count +=1
        m >>= 1
    return count
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()

