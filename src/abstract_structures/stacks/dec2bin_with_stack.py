#!/usr/bin/env python

__author__ = "bt3"


'''transform a decimal number to a binary number with a stack '''


from stack import Stack

def dec2bin_with_stack(decnum):

    s = Stack()
    bits = []

    while decnum > 0:
        dig = decnum % 2
        decnum = decnum//2
        s.push(dig)

    while not s.isEmpty():
        bits.append(str(s.pop()))

    return ''.join(bits) or '0'



if __name__ == '__main__':
    decnum = 9
    assert(dec2bin_with_stack(decnum) == '1001')
    zero = 0
    assert(dec2bin_with_stack(zero) == '0')
