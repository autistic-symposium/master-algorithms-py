#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

def calculate_chain(n):
    n_str = str(n)
    while n_str != 1 or n_str != 89:
        n_str = str(n_str)
        sum_here = 0
        for d in n_str:
            sum_here += int(d)**2
        n_str = sum_here
        if n_str == 89:
            return 1
        if n_str == 1:
            return 0
        

def square_dig_chains(n):
    count = 0
    for i in range(1, n+1):
        count += calculate_chain(i)
    return count
    
   

def main():
    import time
    start = time.time() 

    print(square_dig_chains(10**7))
    
    elapsed = (time.time() - start)
    print('Tests Passed!\n It took %s seconds to run them.' % (elapsed))   
                   
if __name__ == '__main__':
    main()

