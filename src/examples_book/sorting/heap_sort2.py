#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

from heap import Heap

def heap_sort2(seq):
    heap = Heap(seq)
    
    res = []
    for i in range(len(seq)):
        res.insert(0, heap.extract_max())

    return res
    
    
def test_heap_sort2():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    assert(heap_sort2(seq) == sorted(seq))
    print('Tests passed!')


if __name__ == '__main__':
    test_heap_sort2()
