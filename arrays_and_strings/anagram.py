#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


def is_anagram(string1, string2) -> bool:

    string1 = string1.lower()
    string2 = string2.lower()

    if len(string1) != len(string2):
        return False

    for char in string1:
        if char not in string2:
            return False
    
    return True


if __name__ == '__main__':
    
    print('Testing is_anagram()...')
    string1 = "listen"
    string2 = "silent"
    print(f'Is {string1} an anagram of {string2}?: {is_anagram(string1, string2)}')
