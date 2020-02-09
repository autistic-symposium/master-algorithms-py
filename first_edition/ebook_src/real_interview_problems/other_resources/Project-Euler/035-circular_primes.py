#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

def isPrime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    for x in range(2, int(n**0.5)+1):
        if n%x == 0:
            return False
    return True


def findPermutations(s):
    res = []
    if len(s) == 1:
        res.append(s)
    else:
        for i, c in enumerate(s):
            for perm in findPermutations(s[:i] + s[i+1:]):
                res.append(c + perm)
    return res

    



def isCircular(n):
    n_str = str(n)
    permutations = findPermutations(n_str)
    for perm in permutations:
        if not isPrime(perm):
            return False
    return True        
    
 

def generatePrimes(n):
    if n == 2: return [2]
    elif n < 2: return []
    s = [i for i in range(3, n+1, 2)]
    mroot = n ** 0.5
    half = (n+1)//2 - 1
    i, m = 0, 3
    while m <= mroot:
        if s[i]:
            j = (m*m-3)//2
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
        i = i+1
        m = 2*i+3
    return [2]+[x for x in s if x]


def generate_n_Primes(n):
    primes  = []
    chkthis = 2
    while len(primes) < n:
        ptest    = [chkthis for i in primes if chkthis%i == 0]
        primes  += [] if ptest else [chkthis]
        chkthis += 1
    return primes



def circular_primes(n):
    primes = generatePrimes(n)
    count = 0
    for prime in primes:
        if isCircular(prime):
            count += 1
    return count
    

def main():
    import time
    start = time.time() 

    print(circular_primes(1000000))
    
    elapsed = (time.time() - start)
    print('Tests Passed!\n It took %s seconds to run them.' % (elapsed))   
                   
if __name__ == '__main__':
    main()

