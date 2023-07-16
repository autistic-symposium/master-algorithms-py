#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

def find_greatest_common_divider(a, b):
    ''' implements the greatest common divider algorithm '''
    
    while(b != 0):
        result = b
        a, b = b, a % b
    return result


if __name__ == '__main__':

    n1 = 21
    n2 = 7

    print(f'Greatest common divider of {n1} and {n2} is {find_greatest_common_divider(n1, n2)}')
