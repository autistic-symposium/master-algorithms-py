#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

def digit_fifth_pow(n):
    lnum = []   
    for num in range(10**(2), 10**(n+2)):
        sum_here = 0
        num_str = str(num)
        for i in num_str:
            num_int = int(i)
            num_int_pow = num_int**n
            sum_here += num_int_pow 
        if sum_here == num:
            lnum.append(num)
    return lnum, sum(lnum)
   

def main():
    import time
    start = time.time() 
    
    print(digit_fifth_pow(5))
    
    elapsed = (time.time() - start)
    print('Tests Passed!\n It took %s seconds to run them.' % (elapsed))   
                   
if __name__ == '__main__':
    main()

