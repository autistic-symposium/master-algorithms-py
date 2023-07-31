#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

from findstprime import is_prime
   
def summation_primes(n):
    candidate = 2
    prime_set = set()
    while candidate < n:    
        if is_prime(candidate, prime_set):
            prime_set.add(candidate)
        candidate +=1 
    return sum(prime_set)              


def main():
    assert(summation_primes(10) == 17)
    print(summation_primes(2000000))
    print('Tests Passed!')
                   
if __name__ == '__main__':
    main()

