#!/usr/bin/env python

__author__ = "bt3"



def invert_word(word):
    """
    >>> invert_word('buffy is awesome')
    'awesome is buffy'
    """
    new_word = []

    words = word.split(' ')
    for word in words[::-1]:
        new_word.append(word)

    return " ".join(new_word)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

