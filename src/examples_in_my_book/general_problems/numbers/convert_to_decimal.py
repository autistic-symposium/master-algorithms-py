#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail


def convert_to_decimal(number, base):
    ''' convert any number in another base to the decimal base'''
    multiplier, result = 1, 0
    while number > 0:
        result += number%10*multiplier
        multiplier *= base
        number = number//10
    return result


def test_convert_to_decimal():
    number, base = 1001, 2
    assert(convert_to_decimal(number, base) == 9)
    print('Tests passed!')


if __name__ == '__main__':
    test_convert_to_decimal()


