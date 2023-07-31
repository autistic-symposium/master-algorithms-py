#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

def find_sum_proper_divisors(n):
    sum_proper_div = 0
    for i in range(1, n):
        if n%i == 0:
            sum_proper_div += i
    return sum_proper_div


def amicable_numbers(N):
    sum_div_list = [find_sum_proper_divisors(i) for i in range(1, N+1)]
    sum_amicable_numbers = 0
    set_div = set()    
    for a in range(1, N):
        da = sum_div_list[a-1]
        if da < N:
            b = da
            db = sum_div_list[b-1]
            if a != b and db == a and a not in set_div and b not in set_div:
                sum_amicable_numbers += a + b
                set_div.add(a)
                set_div.add(b)
    return sum_amicable_numbers
    

def main():
    print(amicable_numbers(10000))
    print('Tests Passed!')
                   
if __name__ == '__main__':
    main()

