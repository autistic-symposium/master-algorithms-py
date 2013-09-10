#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail


def sum_two_numbers_sequence(seq, s):
    """ given an increasing sorted array and an integer s, find if there is a pair of two numbers in the array whose sum is s. It takes O(n).  """
    l1 = seq[:]
    l2 = seq[:]
    l2.reverse()
    n1 = l1.pop()
    n2 = l2.pop()
    while l2 and l1:
        sum_here = n1 + n2
        if sum_here > s:
            n1 = l1.pop()
        elif sum_here < s:
            n2 = l2.pop()
        else:
            return True
    return False
       


def test_sum_two_numbers_sequence():
    l1 = [1,2,3,4,5,6,7,8]
    s = 7
    assert(sum_two_numbers_sequence(l1, s) == True)
    print('Tests passed!')


if __name__ == '__main__':
    test_sum_two_numbers_sequence()



