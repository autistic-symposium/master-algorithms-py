#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

def convert_from_decimal(number, base):
    ''' convert any decimal number to another base. '''
    multiplier, result = 1, 0
    while number > 0:
        result += number%base*multiplier
        multiplier *= 10
        number = number//base
    return result


def test_convert_from_decimal():
    number, base = 9, 2
    assert(convert_from_decimal(number, base) == 1001)
    print('Tests passed!')


if __name__ == '__main__':
    test_convert_from_decimal()


