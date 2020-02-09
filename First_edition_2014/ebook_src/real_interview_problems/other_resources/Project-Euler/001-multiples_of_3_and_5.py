#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail


def mul3and5(n):
    result = 0
    for num in range(1, n):
        if num%3 == 0 or num%5 == 0:
            result += num
    return result
      
    
    
def test_():
    assert(mul3and5(10) == 23)
    print(mul3and5(1000))
    print('Tests Passed!')
            
if __name__ == '__main__':
    test_()

