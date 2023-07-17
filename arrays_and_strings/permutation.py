#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


def permutation(string) -> list:

    if len(string) == 1:
        return [string]
    
    result = []
    for i, char in enumerate(string):
        for perm in permutation(string[:i] + string[i+1:]):
            result += [char + perm]
    
    return result


if __name__ == '__main__':
    print('Testing permutation()...')
    string = "bt3gl"
    print(f'Permutation of {string}: {permutation(string)}')
