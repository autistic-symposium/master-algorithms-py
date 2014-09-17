#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

''' give all the combinations of a str or list:
    >>> l1 = (1, 2, 3)
    >>> comb_str(l1)
    [[1], [1, [2]], [1, [2, 3]], [1, [3]], [2], [2, 3], [3]]
    >>> comb_str([])
    []
'''



def comb_str(l1):
    if len(l1) < 2: return l1
    result = []
    for i in range(len(l1)):    
        result.append([l1[i]])
        for comb in comb_str(l1[i+1:]):
            result.append([l1[i], comb])
    return result
    
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()

