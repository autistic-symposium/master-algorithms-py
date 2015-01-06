#!/bin/python

'''
Given two strings, write a function
to calculate the longest common prefix (LCP) of the strings.
'''

def lcp(s1, s2):
    '''
    >>> lcp('dabbd', 'aabbaa')
    3
    >>> lcp('abcd', 'hi')
    0
    '''

    p1 = 0
    aux, lcp = '', ''
    string1 = min(s1, s2)
    string2 = max(s1, s2)

    while p1 < len(string1):
        p2 = 0
        while  p2 < len(string2) and p1+p2 < len(string1):
            if string1[p1+p2] == string2[p2]:
                aux += string1[p1+p2]
            else:
                if len(lcp) < len(aux):
                    lcp = aux
                aux = ''
            p2 += 1
        p1 += 1

    return len(lcp)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

