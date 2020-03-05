#!/usr/bin/python

__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"

'''
The rules for writing Roman numerals allow for many ways of writing each number (see About Roman Numerals...). However, there is always a "best" way of writing a particular number.

For example, the following represent all of the legitimate ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

The last example being considered the most efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals; that is, they are arranged in descending units and obey the subtractive pair rule (see About Roman Numerals... for the definitive rules for this problem).

Find the number of characters saved by writing each of these in their minimal form.
'''



import os

def subtractive(roman):
    result = roman
    replacements = [
        ("VIIII", "IX"),
        ("IIII", "IV"),
        ("LXXXX", "XC"),
        ("XXXX", "XL"),
        ("DCCCC", "CM"),
        ("CCCC", "CD"),
    ]
    for old, new in replacements:
        result = result.replace(old, new)
    return result


if __name__ == '__main__':

    current = 0
    improved = 0
    for line in open(os.path.join(os.path.dirname(__file__), 'roman.txt')):
        roman = line.strip()
        current += len(roman)
        improved += len(subtractive(roman))
    print current - improved