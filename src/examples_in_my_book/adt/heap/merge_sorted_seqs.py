#!/usr/bin/python3

# Mari von Steinkirch @ 2013
# mari.wahl9@gmail.com

# Bernardo Sulzbach (mafagafo) @ 2014
# 1449441@gmail.com

import heapq


def merge_sorted_seq(seq1, seq2):
    """
    Merges two sorted sequences with little overhead.
    The result will be sorted, which is different than using the '+' operator.
    """
    result = []
    for c in heapq.merge(seq1, seq2):
        result.append(c)
    return result


def test_merge_sorted_seq(module_name='this module'):
    seq1 = [1, 2, 3, 8, 9, 10]
    seq2 = [2, 3, 4, 5, 6, 7, 9]
    seq3 = seq1 + seq2
    assert merge_sorted_seq(seq1, seq2) == sorted(seq3)
        
    s = 'Tests in {name} have {con}!'
    print(s.format(name=module_name, con='passed'))

if __name__ == '__main__':
    test_merge_sorted_seq()
