#!/bin/python

''' Generate all permutations of an alphanumeric string '''

    def get_permutations(word):
        if len(word) < 2:
            yield word
            return

        for i in range(len(word)):
            rest = word[:i] + word[i+1:]
            for tail in get_permutations(rest):
                yield word[i] + tail



if __name__ == '__main__':
    import doctest
    doctest.testmod()

