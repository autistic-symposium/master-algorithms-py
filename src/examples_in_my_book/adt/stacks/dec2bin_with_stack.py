#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

from stack import Stack

def dec2bin_with_stack(decnum):
    '''transform a decimal number to a binary number with a stack '''
    s = Stack()
    str_aux = ''
    while decnum > 0:
        dig = decnum % 2
        decnum = decnum//2
        s.push(dig)
    while not s.isEmpty():
        str_aux += str(s.pop())
    return str_aux


def test_dec2bin_with_stack(module_name='this module'):
    decnum = 9
    assert(dec2bin_with_stack(decnum) == '1001')
    s = 'Tests in {name} have {con}!'
    print(s.format(name=module_name, con='passed'))


if __name__ == '__main__':
    test_dec2bin_with_stack()
