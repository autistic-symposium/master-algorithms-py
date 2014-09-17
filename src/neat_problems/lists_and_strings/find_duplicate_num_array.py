#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

def find_duplicate_num_array(l1):
    """ an array contains n numbers ranging from 0 to n-1. there are some numbers duplicated, but it is 
    not clear how many. this code find a duplicate number in the array. """
    
    """ A naive solution is to sort the input array, costing O(nlogn). Another solution is the utilization of a hash set. When the number is scanned, it is either in or not. It costs O(n) auxiliary memory to accomodate a hash set. A third solution, that only costs O(1) is consider that indexes in an array with length n are in the range n-1. If there were no duplication in the n numbers from 0 to n-1, we could rearange them sorted, so that each i has its ith number. Since there are duplicates, some locations are occupied by multiple numbers, other are vacant. So every number is scanned one by one, if it the number is not in the right i, it is compared to that from i, and the duplicate can be found, or we swap. Continue until a duplicate is found."""
    
    for i in range(len(l1)):
        if l1[i] == i: continue
        elif l1[i] < 0 or l1[i] > len(l1)-1:
            return None
        elif l1[i] == l1[l1[i]]:  
            return True
        else:
            aux = l1[l1[i]]
            l1[l1[i]] = l1[i]
            l1[i] = aux
    else: 
        return False

def test_find_duplicate_num_array():
    a = [1,3,5,2,4,0]
    b = [1,3,5,2,1,0,4]
    c = [0,0]
    assert(find_duplicate_num_array(b) == True)
    assert(find_duplicate_num_array(a) == False)
    assert(find_duplicate_num_array(c) == True)
    print('Tests passed!')

if __name__ == '__main__':
    test_find_duplicate_num_array()










