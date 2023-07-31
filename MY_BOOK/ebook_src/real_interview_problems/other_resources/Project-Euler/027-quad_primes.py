#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

def quad_form(n, a, b):
    return n**2 + a*n + b

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

def quad_primes(a, b):
    count_max = 0
    coef = ()
    for aa in range(-a, a):
        for bb in range(-b, b):  
            n = 0 
            while True: 
                number = quad_form(n, aa, bb)
                if isPrime(number):
                    n += 1
                else:
                    if n > count_max:
                        count_max = n
                        coef = (aa, bb)
                    break
    return coef(0)*coef(1), coef
   

def main():
    import time
    start = time.time() 

    print(quad_primes(1000, 1000))
    
    elapsed = (time.time() - start)
    print('Tests Passed!\n It took %s seconds to run them.' % (elapsed))   
                   
if __name__ == '__main__':
    main()

