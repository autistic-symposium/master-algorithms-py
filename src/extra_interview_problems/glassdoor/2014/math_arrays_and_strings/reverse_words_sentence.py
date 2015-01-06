#!/usr/bin/env python

__author__ = "bt3"


def reversing_words_setence_py(s):
    words = s.split()
    return ' '.join(reversed(words))

def reversing_words_setence_py2(s):
    words = s.split(' ')
    words.reverse()
    return ' '.join(words)

def reversing_words_setence_py3(s):
    p1 = 0
    word = ''
    arr = []
    while p1 < len(s):
        if s[p1] != ' ':
            word += s[p1]
        else:
            arr.append(word)
            word = ''
        p1 += 1

    arr.append(word)
    new = ''
    while arr:
        new += arr.pop()
        new += ' '

    return new




if __name__ == '__main__':
    s = "Buffy is a Vampire Slayer"
    print reversing_words_setence_py(s)
    print reversing_words_setence_py2(s)
    print reversing_words_setence_py3(s)


