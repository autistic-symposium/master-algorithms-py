#!/bin/python

'''
find prime factors of a number.
'''

import math

def find_prime_factors(n):
    '''
    >>> find_prime_factors(14)
    [2, 7]
    >>> find_prime_factors(19)
    []
    '''

    divisors = [d for d in range(2, n//2 + 1) if n % d == 0]
    primes = [d for d in divisors if is_prime(d)]

    return primes


def is_prime(n):
    for j in range(2, int(math.sqrt(n))):
        if (n % j) == 0:
            return False
    return True



if __name__ == '__main__':
    import doctest
    doctest.testmod()

