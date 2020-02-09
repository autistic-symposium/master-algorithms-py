#!/usr/bin/python


__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"

'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
'''



def isPandigitalString(string):
    """ Check if string contains a pandigital number. """
    digits = len(string)

    if digits >= 10:
        return False

    for i in range(1,digits+1):
        if str(i) not in string:
            return False
    return True



def gives9PandigitalProduct(a, b):
    numbers = str(a) + str(b) + str(a*b)
    if len(numbers) != 9:
        return False
    return isPandigitalString(numbers)


def main():
    products = []

    for a in range(0, 100000):
        for b in range(a, 100000):
            if len(str(a*b) + str(a) + str(b)) > 9:
                break
            if gives9PandigitalProduct(a, b):
                products.append(a*b)
                print("%i x %i = %i" % (a, b, a*b))

    print(sum(set(products)))


if __name__ == '__main__':
    main()
