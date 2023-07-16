#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

def fibonacci(n):
    """ Calculate the nth Fibonacci number """
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':

    print('Testing fibonacci')
    n = 10
    print(f'Fibonacci of {n}: {fibonacci(n)}')
