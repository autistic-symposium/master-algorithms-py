#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

import math

def find_fibonacci_seq_rec(n):
    ''' implements the nth fibonacci value in a recursive exponential runtime '''
    if n < 2: return n
    return find_fibonacci_seq_rec(n - 1) + find_fibonacci_seq_rec(n - 2)
    
    

def find_fibonacci_seq_iter(n):
    ''' return the nth fibonacci value in a iterative O(n^2) runtime '''
    if n < 2: return n
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def find_fibonacci_seq_form(n):
    ''' return the nth fibonacci value implemented by the formula, nearly constant-time algorithm,
    but, it has a poor precise (after 72 it starts to become wrong) '''
    sq5 = math.sqrt(5)
    phi = (1 + sq5) / 2
    return int(math.floor(phi ** n / sq5))
    
    
    
def test_find_fib():
    n = 10
    assert(find_fibonacci_seq_rec(n) == 55)
    assert(find_fibonacci_seq_iter(n) == 55)
    assert(find_fibonacci_seq_form(n) == 55)
    print('Tests passed!')



if __name__ == '__main__':
    test_find_fib()

        
