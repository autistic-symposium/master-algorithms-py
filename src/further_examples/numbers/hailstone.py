# The Hailstone sequence of numbers can be generated from a starting positive integer n by:
#   If n is 1 then the sequence ends.
#   If n is even then the next n of the sequence = n/2
#   If n is odd then the next n of the sequence = (3 * n) + 1

# The (unproven) Collatz conjecture is that the hailstone sequence for any starting number always terminates.

# Coded by Bernardo Sulzbach (mafagafogigante@gmail.com) [github.com/mafagafo]


def hailstone(n):
    """
    Generates the Hailstone sequence for n.
    :param n: the starting positive integer.
    :rtype : list
    :return: the generated sequence.
    """
    assert isinstance(n, int), 'n must be an integer.'
    assert n > 0, 'n must be a positive integer.'
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
    sequence.append(1)
    return sequence


def hailstone_elements(n):
    """
    The number of elements in the Hailstone sequence for n.
    :param n: the starting positive integer.
    :rtype : integer
    :return: the number of elements in the generated sequence.
    """
    assert isinstance(n, int), 'n must be an integer.'
    assert n > 0, 'n must be a positive integer.'
    elements = 1
    while n != 1:
        elements += 1
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
    return elements


def biggest_hailstone_below_n(n):
    """
    Returns the biggest value below n that produces the biggest Hailstone sequence and the size of this sequence.
    :rtype : tuple
    :return: the biggest value below n that produces the biggest Hailstone sequence and the size of this sequence.
    """
    assert isinstance(n, int), 'n must be an integer.'
    assert n > 1, 'n must be an integer bigger than 1.'
    best, biggest = 1, 1
    for i in range(2, n):
        count = hailstone_elements(i)
        if count > biggest:
            best, biggest = i, count
    return best, biggest


def test_functions():
    assert hailstone_elements(27) == 112
    assert hailstone(27)[:4] == [27, 82, 41, 124] and hailstone(27)[-4:] == [8, 4, 2, 1]
    assert biggest_hailstone_below_n(100000) == (77031, 351)


if __name__ == '__main__':
    print('The Hailstone sequence for 14: ' + ', '.join((str(i) for i in hailstone(14))))
    print('The Hailstone sequence for 1414 has', hailstone_elements(1414), 'elements.')