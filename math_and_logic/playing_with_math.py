#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

import math
import random


def find_greatest_common_divider(a, b) -> int:
    '''Implements the greatest common divider algorithm '''
    
    while(b != 0):
        result = b
        a, b = b, a % b
        
    return result


def _is_prime(number) -> bool:
    '''Check if a number is prime '''

    if number < 2:
        return False

    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            return False
    
    return True


def find_prime_factors(number) -> list:
    '''Find prime factors of a number '''
    
    divisors = [d for d in range(2, number//2 + 1) if number % d == 0]
    primes = [d for d in divisors if _is_prime(d)]

    return primes



if __name__ == '__main__':

    n1 = 21
    n2 = 7

    print(f'Greatest common divider of {n1} and {n2} is {find_greatest_common_divider(n1, n2)}')
    print(f'Prime factors of {n1} are {find_prime_factors(n1)}')


