#!/usr/bin/env python

__author__ = "bt3"

''' Generate all permutations of an alphanumeric string '''

def permutations(word):
    '''
    >>> permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    >>> permutations('')
    ''
    '''
    if len(word) < 2:
        return word

    res = []
    for i in range(len(word)):
        rest = word[:i] + word[i+1:]
        for p in permutations(rest):
            res.append(word[i] + p)
    return res



if __name__ == '__main__':
    import doctest
    doctest.testmod()

