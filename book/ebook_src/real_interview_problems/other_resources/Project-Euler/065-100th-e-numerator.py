#!/usr/bin/python

__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"

'''
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:

2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
'''

from itertools import islice

def take(iterable, n):
    #Make an iterator that returns selected elements from the iterable.
    return list(islice(iterable, n))

def e():
    yield 2
    k = 1
    while True:
        yield 1
        yield 2*k
        yield 1
        k += 1

def rationalize(frac):
    if len(frac) == 0:
        return (1, 0)
    elif len(frac) == 1:
        return (frac[0], 1)
    else:
        remainder = frac[1:len(frac)]
        (num, denom) = rationalize(remainder)
        return (frac[0] * num + denom, num)

numerator = rationalize(take(e(), 100))[0]
print sum(int(d) for d in str(numerator))