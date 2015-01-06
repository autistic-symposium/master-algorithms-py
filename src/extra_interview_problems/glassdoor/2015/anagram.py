#!/bin/python

from collections import Counter

def is_anagram(s1, s2):
    '''
    >>> is_anagram('cat', 'tac')
    True
    >>> is_anagram('cat', 'hat')
    False
    '''
    counter = Counter()
    for c in s1:
        counter[c] += 1

    for c in s2:
        counter[c] -= 1

    for i in counter.values():
        if i:
            return False

    return True




if __name__ == '__main__':
    import doctest
    doctest.testmod()

