#!/usr/bin/env python

def define_if_permutation(word1, word2):
    """
    >>> define_if_permutation('hello', 'lolhe')
    True
    >>> define_if_permutation('stripe', 'triipe')
    False
    """
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False






if __name__ == '__main__':
    import doctest
    doctest.testmod()