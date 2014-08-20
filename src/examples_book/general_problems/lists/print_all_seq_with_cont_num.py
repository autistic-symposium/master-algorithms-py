#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail


def print_all_seq_with_cont_num(s):
    ''' print all sequences with cont. numbers (2 at least) whose sum is a given s '''
    if s < 3: return s
    small = 1
    big =  2
    sum_here = big + small
    result = []
    
    while small < (1+s)/2:
        sum_here = sum(range(small, big))
        if sum_here < s:
            big += 1
        elif sum_here > s:
            small +=1
        else:
            result.append(list(range(small, big)))
            big += 1
       
    return result

def test_print_all_seq_with_cont_num():
    s = 15
    sum_set_for_s = [[1,2,3,4,5], [4,5,6], [7,8]]
    assert(print_all_seq_with_cont_num(s) == sum_set_for_s)
    s = 1
    assert(print_all_seq_with_cont_num(s)== 1)    
    s = 0
    assert(print_all_seq_with_cont_num(s) == 0)  
    print('Tests passed!')


if __name__ == '__main__':
    test_print_all_seq_with_cont_num()

