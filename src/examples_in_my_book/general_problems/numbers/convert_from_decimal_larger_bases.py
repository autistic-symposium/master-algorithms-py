#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail


def convert_from_decimal_larger_bases(number, base):
    ''' convert any decimal number to a number in a base up to 20'''
    strings = "0123456789ABCDEFGHIJ"
    result = ""
    while number > 0:
        digit = number%base
        result = strings[digit] + result
        number = number//base
    return result

def test_convert_from_decimal_larger_bases():
    number, base = 31, 16
    assert(convert_from_decimal_larger_bases(number, base) == '1F')
    print('Tests passed!')

if __name__ == '__main__':
    test_convert_from_decimal_larger_bases()


