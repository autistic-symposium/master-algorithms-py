#!/usr/bin/env python

__author__ = "bt3"


def combinations(s):
    '''
    >>> combinations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    >>> combinations('')
    ''
    '''
    if len(s) < 2:
        return s
    res = []
    for i, c in enumerate(s):
        res.append(c)
        for j in combinations(s[:i] + s[i+1:]):
            res.append(c + j)
    return res



if __name__ == '__main__':
    import doctest
    doctest.testmod()
