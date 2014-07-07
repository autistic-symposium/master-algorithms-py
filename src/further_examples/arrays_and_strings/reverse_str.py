# Mari von Steinkirch @ 2013
# mari.wahl9@gmail.com

# Bernardo Sulzbach (mafagafo) @ 2014
# 1449441@gmail.com

# This file defines and compares four different functions that reverse a string.

# timeit is used for benchmarking.
from timeit import timeit


def reverse_1(string):
    """
    Slowest function. Use a list and str.join to reverse the string.
    :param string: the string to be reversed.
    :return: a reversed string.
    """
    reversed_string = []
    # Iterates from the last to the first character.
    for i in range(len(string) - 1, -1, -1):
        # Appends the character to the list.
        reversed_string.append(string[i])
    return ''.join(reversed_string)


def reverse_2(string):
    """
    Same principle as reverse_1. One-liner cousin.
    :param string: the string to be reversed.
    :return: a reversed string.
    """
    return ''.join([character for character in [string[i] for i in range(len(string) - 1, -1, -1)]])


def reverse_3(string):
    """
    Another one-liner. We make a list from the characters of the string and reverse it.
    :param string: the string to be reversed.
    :return: a reversed string.
    """
    return ''.join([character for character in string][::-1])

# Overkill of elegance. A bit too passionate but it defines this lambda function well.
# Simply returns the string backwards. As fast as concise.
reverse_lambda = lambda s: s[::-1]

# We define some short strings to test our functions.
strings = ('buffy', 'foo', 'bar')
# We announce what we are doing.
print(', '.join(strings), ' should appear reversed if the function is working.\n')
print('{:<30}:'.format('Function name'), 'benchmarking result (lower is better):')
# Iterate over a tuple of functions.
for function in (reverse_1, reverse_2, reverse_3, reverse_lambda):
    name = function.__name__ if function.__name__ != "<lambda>" else 'reverse_lambda'
    # We print the function's name and its benchmark result.
    print("{:<30}:".format(name), timeit(name + "('string')", setup='from __main__ import ' + name))
    # We print the output so that we can check if the function is working as expected.
    print(', '.join(map(function, strings)), '\n')
# We wait until the user wants to quit.
input('Press Return to quit.')
