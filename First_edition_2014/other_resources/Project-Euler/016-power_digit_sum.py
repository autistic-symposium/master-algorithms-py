#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail


def power_digit_sum(n):
    number = str(2**n)
    sum_res = 0
    for i in number:
        sum_res += int(i)
    return sum_res
      
    
    
def test_():
    assert(power_digit_sum(15) == 26)
    print(power_digit_sum(1000))
    print('Tests Passed!')
            
if __name__ == '__main__':
    test_()

