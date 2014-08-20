#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

''' give all the permutation of a str:
    >>> str1 = 'hat'
    >>> perm_str(str1)
    ['hat', 'hta', 'aht', 'ath', 'tha', 'tah']
    >>> perm_str('')
    ''
'''

def perm_str(str1):
    if len(str1) < 2: return str1
    result = []
    for i in range(len(str1)):       
        for perm in perm_str(str1[:i] + str1[i+1:]):
            result.append(str1[i] + perm)
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()

