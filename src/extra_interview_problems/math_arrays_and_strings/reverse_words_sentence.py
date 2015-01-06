#!/usr/bin/env python

__author__ = "bt3"


def reversing_words_setence_py(s):
    words = s.split()
    return ' '.join(reversed(words))

def reversing_words_setence_py2(s):
    words = s.split(' ')
    words.reverse()
    return ' '.join(words)





if __name__ == '__main__':
    s = "Buffy is a Vampire Slayer"
    print reversing_words_setence_py(s)
    print reversing_words_setence_py2(s)


