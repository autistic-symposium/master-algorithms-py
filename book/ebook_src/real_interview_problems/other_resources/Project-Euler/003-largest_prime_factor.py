#!/usr/bin/python3
#!/usr/bin/python3

def is_prime(n):
    if n < 4 : return True
    for i in range(2, int(n**0.5 + 1)):
        if not n%i: return False
    return True


def largest_prime_factor(n):
    i = int(n**0.5 +1)
    while i > 1 :
        if not n%i and i&1: 
            if is_prime(i): return i
        i -= 1
    return None


def largest_prime_factor_optimized(n):
    factor = 2
    lastfactor = 1
    while n > 1:
        if not n%factor:
            lastfactor = factor
            n = n//factor
            while n%factor == 0:
                n = n//factor
        factor += 1      
    return lastfactor


def test_largest_prime_factor():
    assert(largest_prime_factor(13195)== 29)
    print(largest_prime_factor(600851475143))  
    assert(largest_prime_factor_optimized(13195) == 29)
    print(largest_prime_factor_optimized(600851475143))  
    print('Tests Passed!')
            
if __name__ == '__main__':
    test_largest_prime_factor()
