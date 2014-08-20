#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail



def quick_sort(seq):
    if len(seq) < 2: return seq
    pivot = sorted(seq[0], seq[len(seq)//2], seq[-1])[1]
    print(pivot)
    left = quick_sort([x for x in seq[1:] if x < pivot])
    right = quick_sort([x for x in seq[1:] if x >= pivot])
    return left + [pivot] + right
    
    
""" we can also divide them into two functions """
def partition(seq):
    pi,seq = seq[0],seq[1:]                     
    lo = [x for x in seq if x <= pi]            
    hi = [x for x in seq if x > pi]             
    return lo, pi, hi 

def quick_sort_divided(seq):
    if len(seq) < 2: return seq                
    lo, pi, hi = partition(seq)                  
    return quick_sort_divided(lo) + [pi] + quick_sort_divided(hi)


   

def test_quick_sort():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    assert(quick_sort(seq) == sorted(seq))
    assert(quick_sort_divided(seq) == sorted(seq))
    print('Tests passed!')


if __name__ == '__main__':
    test_quick_sort()



