#!/bin/python

"""
Write a function fib() that takes an integer nn and returns the nnth Fibonacci number.
"""

# this is O(2^n)
def fib(n):
    if n in [1, 0]:
        return n
    return fib(n - 1) + fib(n - 2)
    

print fib(10)


# this is O(n)
def fib(n):
    if n < 0:
        raise ValueError('Index was negative. No such thing as a '
                         'negative index in a series.')
    elif n in [0, 1]:
        return n

    prev_prev = 0  # 0th fibonacci
    prev = 1       # 1st fibonacci

    for _ in range(n - 1):
        current = prev + prev_prev
        prev_prev = prev
        prev = current

    return current
        

print fib(10)