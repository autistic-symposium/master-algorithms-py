#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail


def rotating_array(seq, N):
    ''' rotate an array from right to left for a given number'''
    myqueue = []
    for i in range(N):
        myqueue.append(seq.pop())
    myqueue.reverse()
    return myqueue + seq



def test_rotating_array(module_name='this module'):
    seq = [1, 2, 3, 4, 5, 6, 7]
    N = 4
    assert(rotating_array(seq, N) == [4, 5, 6, 7, 1, 2, 3])
        
    s = 'Tests in {name} have {con}!'
    print(s.format(name=module_name, con='passed'))


if __name__ == '__main__':
    test_rotating_array()

