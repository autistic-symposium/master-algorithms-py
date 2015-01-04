#!/usr/bin/python

'''
    swapping values in place without extra memory
'''


def swap_bit(a, b):
    a = a^b
    b = a^b
    a = a^b
    return a, b


if __name__ == '__main__':
    a = 14
    b = 73
    a2, b2 = swap_bit(a, b)
    print "a was {0}, now it is {1}. \nb was {2}, now it is {3}".format(a, a2, b, b2)
