#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

   
def sum_square_diff(n):
    sq_sum, sum_sq = 0, 0
    for i in range(1, n+1):
        sum_sq += i**2
        sq_sum += i
    sq_sum = sq_sum **2
    return sq_sum - sum_sq

def main():
    assert(sum_square_diff(10) == 2640)
    print(sum_square_diff(100))
    print('Tests Passed!')
                   
if __name__ == '__main__':
    main()

