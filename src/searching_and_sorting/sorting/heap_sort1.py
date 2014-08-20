#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

import heapq

def heap_sort1(seq):
    ''' heap sort with Python's heapq '''
    h = []
    for value in seq:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]


def test_heap_sort1():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    assert(heap_sort1(seq) == sorted(seq))
    print('Tests passed!')


if __name__ == '__main__':
    test_heap_sort1()

