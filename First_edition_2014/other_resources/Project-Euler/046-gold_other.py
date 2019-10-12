#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

def isPrime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True


def generetePrimes(n):
    if n == 2: return [2]
    elif n < 2: return []
    s = [i for i in range(3, n+1,2)]
    mroot = n ** 0.5
    half = (n+1)//2-1
    i = 0
    m = 3
    while m <= mroot:
        if s[i]:
            j = (m*m - 3)//2
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
        i = i+1
        m = 2*i+3
    return [2]+[x for x in s if x]


def gold_other(n):
    primes_for_n = generetePrimes(n)
    numbers = {prime + 2*x**2 for prime in primes_for_n for x in range(1, int(n**0.5))}
    conj = {x for x in range(3, n, 2) if not isPrime(x)}
    
    while True:
        candidates = conj - numbers
        if not candidates:
            gold_other(2*n)
        else:
            return min(candidates)

   

def main():
    import time
    start = time.time() 

    print(gold_other(10000))
    
    elapsed = (time.time() - start)
    print('Tests Passed!\n It took %s seconds to run them.' % (elapsed))   
                   
if __name__ == '__main__':
    main()

