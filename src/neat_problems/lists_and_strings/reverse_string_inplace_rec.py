#!/usr/bin/env python

author = "Mari Wahl"
email = "marina.w4hl@gmail.com"



def reverse_string_inplace_rec(s):
    ''' takes a string and returns its reverse'''
    if s:
        s = s[-1] + reverse_string_inplace_rec(s[:-1])
    return s

def reverse_string_inplace(s):
    s = s[::-1]
    if s[0] == '\0':
        s = s[1:]
        s += '\0'
    return s



def test_reverse_string_inplace_rec(module_name='this module'):
    s = 'hello'
    s2 = 'buffy\0'
    assert(reverse_string_inplace(s) == 'olleh')
    assert(reverse_string_inplace(s2) == 'yffub\0')
    assert(reverse_string_inplace_rec(s) == 'olleh')

    s = 'Tests in {name} have {con}!'
    print(s.format(name=module_name, con='passed'))

if __name__ == '__main__':
    test_reverse_string_inplace_rec()

