#!/usr/bin/env python

__author__ = "bt3"


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



def lcppy(x):
    '''
    >>> lcppy([[3,2,1], [3,2,1,4,5]])
    [3, 2, 1]
    '''
    import os
    return os.path.commonprefix(x)


def lcp2(s1, s2):
    '''
    >>> lcp2('dabbd', 'aabbaa')
    3
    >>> lcp2('abcd', 'hi')
    0
    '''
    m = [[0 for i in range(len(s2) + 1)] for k in range(len(s1) + 1)]

    lcp = 0

    for y in range(1, len(s1) + 1):
        for x in range(1, len(s2) + 1):
            if (s1[y - 1] == s2[x - 1]):
                m[y][x] = m[y - 1][x - 1] + 1
            else:
                m[y][x] = 0

            if m[y][x] > lcp:
                lcp = m[y][x]
    return lcp



if __name__ == '__main__':
    import doctest
    doctest.testmod()

