#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

import math

def find_div(n):
    ''' find the divisor of a given n'''
    set_div = {1, n}   
    for i in range(2, int(math.sqrt(n))+ 1):
        if not n % i:
            set_div.add(i)
            set_div.add(n//i) 
    l1 = list(set_div)
    return len(l1)
    
    
def find_trian(l):
    ''' find the lth trian number'''
    return sum(range(1, l+1))


def highly_divisible_trian_num(d):
    thtriangle, n_div, count = 1, 0, 1
    while n_div < d:
        count += 1
        thtriangle += count
        n_div = find_div(thtriangle)
    return (thtriangle, count)
                
    
def main():
    import time
    start = time.time()   
    assert(highly_divisible_trian_num(6) == (28, 7))
    print(highly_divisible_trian_num(500))
    
    elapsed = (time.time() - start)
    print('Tests Passed!\n It took %s seconds to run them.' % (elapsed))   
                   
if __name__ == '__main__':
    main()

