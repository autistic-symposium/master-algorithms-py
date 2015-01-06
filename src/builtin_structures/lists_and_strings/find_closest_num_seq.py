#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail



def find_closest_num_seq_unsorted(seq):
    ''' Find the Closest two Numbers in a Sequence. If we do this without sorting 
        first, the runtime will be O(n^2) '''
    dd = float("inf")
    for x in seq:
        for y in seq:
            if x == y: continue
            d = abs(x - y)
            if d < dd:
                xx, yy, dd = x, y, d	
    return xx, yy


def find_closest_num_seq_sorted(seq):
    ''' However, if we sort first, we can achieve it with runtime O(n log n): '''
    seq.sort()
    print(seq)
    dd = float("inf")
    for i in range(len(seq) - 1):
        x, y = seq[i], seq[i+1]
        if x == y: continue
        d = abs(x-y)
        if d < dd:
            xx, yy, dd = x, y, d
    return xx, yy
		

def test_find_closest_num_seq(module_name='this module'):
    import random
    seq = [random.randrange(100) for i in range(20)]
    print(seq)	
    print(find_closest_num_seq_sorted(seq))
    print(find_closest_num_seq_unsorted(seq))
           
    s = 'Tests in {name} have {con}!'
    print(s.format(name=module_name, con='passed'))


if __name__ == '__main__':
    test_find_closest_num_seq()

