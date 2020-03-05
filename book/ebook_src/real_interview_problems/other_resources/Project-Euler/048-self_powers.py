#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

def self_powers(power, digits):
    sum_total = 0
    for pow in range(1, power+1):
        sum_total += pow**pow
    sum_total_str = str(sum_total)
    last_digits = ''
    for i, c in enumerate(sum_total_str[-digits:]):
        last_digits += c
    return int(last_digits)


def main():
    import time
    start = time.time() 
    
    
    assert(self_powers(10, len('10405071317')) == 10405071317)
    print(self_powers(1000, 10))
    
    elapsed = (time.time() - start)
    print('Tests Passed!\n It took %s seconds to run them.' % (elapsed))   
                   
if __name__ == '__main__':
    main()

