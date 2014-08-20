#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

def find_max_subarray1(l1):
    ''' calculate the greatest sum of subarrays from an array. 
    An array with n elements has n(n+1)/2 subarrays so force brute cost O(n^2).
    What we can do is to check when a sum becomes a negative number or zero, and then discard, since  
    this will not "add" anything to the new event... When the sum decreases, it gets the previous sum. '''
    sum_new, result = 0, 0
    for c in l1:
        result = max(result, sum_new)
        sum_new += c
        if sum_new <= 0: sum_new = 0        
    return result



def find_max_subarray2(l1):
    ''' find the contiguous subarray which has the largest sum (Kadane's algorithm in O(n)) 
        with extra O(n) space '''
    sum_old = [l1[0]]
    for c in l1:
        sum_old.append(max(c, sum_old [-1] + c))
    return max(sum_old)


def test_find_max_subarray():
    l1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    l2 = [-1, 3, -5, 4, 6, -1, 2, -7, 13, -3]
    assert(find_max_subarray1(l1)) == 6)
    assert(find_max_subarray1(l2)) == 17)
    assert(find_max_subarray2(l1) == 6)
    assert(find_max_subarray2(l2) == 17)
    print('Tests passed!')

if __name__ == '__main__':
    test_find_max_subarray()






