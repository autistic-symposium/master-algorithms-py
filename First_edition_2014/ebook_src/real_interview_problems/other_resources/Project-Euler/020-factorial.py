#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

def factorial(n):
    prod = 1
    for i in range(1,n):
        prod *= i
    return prod

def find_sum(n):
    sum_ = 0
    fact = factorial(n)
    number = str(fact)
    for i in number:
        sum_ += int(i)
    return sum_


def main():
    import time
    start = time.time() 
    
    assert(find_sum(10) == 27)  
    print(find_sum(100))
    
    elapsed = (time.time() - start)
    print('Tests Passed!\n It took %s seconds to run them.' % (elapsed))   
                   
if __name__ == '__main__':
    main()

