#!/usr/bin/env python

__author__ = "bt3"


from collections import defaultdict


def find_unique_number(arr):
    table = defaultdict(int)
    total = 0
    for i in arr:
        if table[i]:
            total -= i
        else:
            total += i
            table[i] +=1
    return total


def find_unique_number_xor(arr):
    xor = 0
    for item in arr:
        xor ^= item
    return xor


def find_unique_char(s):
    if len(s) < 2: return True
    for i, c in enumerate(s):
        for j in s[i+1:]:
            if j == c:
                return False
    return True



if __name__ == '__main__':
    arr = [1, 3, 5, 6, 1, 5, 6, 3, 7,]
    print(find_unique_number(arr))
    print(find_unique_number_xor(arr))
    s1 = 'abcdefg'
    s2 = 'buffy'
    s3 = ''
    print
    print(find_unique_char(s1))
    print(find_unique_char(s2))
    print(find_unique_char(s3))
