#!/usr/bin/python3

#  Mari von Steinkirch @ 2013
# mari.wahl9@gmail.com

# Bernardo Sulzbach (mafagafo) @ 2014
# 1449441@gmail.com


def bubble_sort(seq):
    """
    Implementation of bubble sort.
    O(n²) and thus highly ineffective.
    :param seq: the sequence to be sorted.
    :return: the sorted sequence.
    """
    size = len(seq) -1
    for num in range(size, 0, -1):
        for i in range(num):
            if seq[i] > seq[i+1]:
                temp = seq[i]
                seq[i] = seq[i+1]
                seq[i+1] = temp
    return seq


def test_bubble_sort(module_name='this module'):
    seq = [4, 5, 2, 1, 6, 2, 7, 10, 13, 8]
    assert(bubble_sort(seq) == sorted(seq))
        
    s = 'Tests in {name} have {con}!'
    print(s.format(name=module_name, con='passed'))


if __name__ == '__main__':
    test_bubble_sort()

