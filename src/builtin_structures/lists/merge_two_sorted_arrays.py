#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

def merge_two_sorted_arrays(a1, a2):
    """ merge two sorted arrays, keeping the final sorted """
    if len(a1) >= len(a2): 
        biga = a1
        smalla = a2
    else: 
        biga = a2
        smalla = a1
    final = []
    count = 0
    for i in range(len(biga)):
        if count < len(smalla) and smalla[count] < biga[i]:
            final.append(smalla[count]) 
            count+=1
        final.append(biga[i])
    return final

def test_merge_two_sorted_arrays():
    a1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    a2 = [3, 6, 7]
    assert(merge_two_sorted_arrays(a1, a2) == [0, 1, 2, 3, 3, 4, 5, 6, 6, 7, 7, 8, 9, 10])
    print('Tests passed!')

if __name__ == '__main__':
    test_merge_two_sorted_arrays()







            
              
