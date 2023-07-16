#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

def reverse_array_in_place(array):
    """ Reverse an array in place """
    return array[::-1]


if __name__ == '__main__':

    print('Testing reverse_array_in_place')
    array = [1, 2, 3, 4, 5]
    print(f'Array: {array}')
    print(f'Reversed: {reverse_array_in_place(array)}')
