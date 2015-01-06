#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail


def find_max_profit_On(seq):
    ''' find the most profit from a seq with O(n) '''
    max_profit = 0
    min_value = seq[0]
    for i in range(1, len(seq)):
        profit_here = seq[i]- min_value
        if profit_here > max_profit:
            max_profit = profit_here
        else:
            if min_value > seq[i]:
                min_value = seq[i]
                   
    return max_profit


def find_max_profit_On2(seq):
    ''' find the most profit from a seq with O(n2) '''
    max_profit = 0
    for i in range(len(seq)-1):
        for j in range (i, len(seq)-1):
            if seq[j] - seq[i] > max_profit: 
                max_profit = seq[j] - seq[i]
    return max_profit
                

def test_find_max_profit():
    seq = [9,11,5,7,16,1] 
    assert(find_max_profit_On(seq) == 11)
    assert(find_max_profit_On2(seq) == 11)
    seq = [1,15,2,3,4,3]
    assert(find_max_profit_On(seq) == 14)
    assert(find_max_profit_On2(seq) == 14)
    print('Tests passed!')


if __name__ == '__main__':
    test_find_max_profit()


