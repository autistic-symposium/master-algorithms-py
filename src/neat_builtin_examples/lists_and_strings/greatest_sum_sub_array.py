#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail


def greatest_sum_sub_array(l1):
    sum_new = 0
    results = []
    for i, c in enumerate(l1):
        sum_old = sum_new
        sum_new = sum_old + c
        if sum_new <= 0 or sum_new < sum_old:
            sum_new = 0
            results.append(sum_old)     
            continue
    results.append(sum_new)
    results.sort()
    return results.pop()

def test_greatest_sum_sub_array():
    l1 = [1, -4, 20, -4, 5, 15, 3]
    assert(greatest_sum_sub_array(l1) == 23)
    print('Tests passed!')

if __name__ == '__main__':
    test_greatest_sum_sub_array()

