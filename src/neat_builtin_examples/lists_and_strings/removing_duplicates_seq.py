#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail


def removing_duplicates_seq(seq):
    ''' if the values are hashable, we can use set and generators to remove duplicates
        in a sequence '''
    seen = set()
    for item in seq:
        if item not in seen:
            yield item
            seen.add(item)

def removing_duplicates_seq_not_hash(seq, key= None):
    ''' if the item is not hashable, such as dictionaries '''
    seen = set()
    for item in seq:
        val = item if key is None else key[item]
        if item not in seen:
            yield item
            seen.add(val)
    


def test_removing_duplicates_seq():
    seq = [1, 2, 2, 2, 3, 3, 4, 4, 4]
    dict = {'a':1, 'b':2, 'a':2, 'a':1}
    assert(list(removing_duplicates_seq(seq)) == [1,2,3,4])
    assert(list(removing_duplicates_seq_not_hash(dict)) == ['a', 'b'])
    print('Tests passed!'.center(20, '*'))
    

if __name__ == '__main__':
    test_removing_duplicates_seq()


