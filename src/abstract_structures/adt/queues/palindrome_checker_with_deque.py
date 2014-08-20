#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

import sys
import string
import collections  

def palindrome_checker_with_deque(str1):
    d = collections.deque()
    eq = True
    strip = string.whitespace + string.punctuation + "\"'" 
    for s in str1.lower():
        if s not in strip: d.append(s)
    while len(d) > 1 and eq:
        first = d.pop()
        last = d.popleft()
        if first != last:
            eq = False
    return eq
  

def test_palindrome_checker_with_deque():
    str1 = 'Madam Im Adam'
    str2 = 'Buffy is a Slayer'
    assert(palindrome_checker_with_deque(str1) == True)
    assert(palindrome_checker_with_deque(str2) == False)
    print('Tests passed!')


if __name__ == '__main__':
        test_palindrome_checker_with_deque()   


