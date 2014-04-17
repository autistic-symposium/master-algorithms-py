#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

''' --> In the case of two arrays: we can merge two arrays using the merge function from the merge sort
    --> we can do this for files too, merging each two

        1) If we can modify the arrays (pop) we can use:
            def merge(left, right):
                if not left or not right: return left or right # nothing to be merged
                result = []
                while left and right:
                    if left[-1] >= right[-1]:
                        result.append(left.pop())
                    else:
                        result.append(right.pop())
                result.reverse()
                return (left or right) + result
        
        
        2) If we can't modify or we want to in place, we need two pointers:
        >>> l1 = [1, 2, 3, 4, 5, 6, 7]
        >>> l2 = [2, 4, 5, 8]
        >>> merge(l1, l2)
        [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 8]
    
    
        3) For example, in the case we have a big array filled 0s in the end, and another array with the size of the number of 0s:
        >>> l1 = [1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0]
        >>> l2 = [2, 4, 5, 8]
        >>> merge_two_arrays_inplace(l1, l2)
        [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 8]
        
        
        4) If we want to merge sorted files (and we have plenty of RAM to load all files):
        >>> list_files = ['1.dat', '2.dat', '3.dat']
        >>> merge_files(list_files)
        [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8]
''' 

def merge(left, right):
    if not left or not right: return left or right # nothing to be merged
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if left[i:] : result.extend(left[i:])   # REMEMBER TO TO ENXTEND NOT APPEND
    if right[j:] : result.extend(right[j:])
    return result


 
def merge_two_arrays_inplace(l1, l2):
    if not l1 or not l2: return l1 or l2 # nothing to be merged
    p2 = len(l2) - 1    
    p1 = len(l1) - len(l2) - 1   
    p12 = len(l1) - 1
    while p2 >= 0 and p1 >= 0:
        item_to_be_merged = l2[p2]
        item_bigger_array = l1[p1]       
        if item_to_be_merged < item_bigger_array:
            l1[p12] = item_bigger_array
            p1 -= 1
        else:
            l1[p12] = item_to_be_merged
            p2 -= 1
        p12 -= 1
    return l1


def merge_files(list_files):
    result = []
    final = []
    for filename in list_files:
        aux = []
        with open(filename, 'r') as file:
            for line in file:
                aux.append(int(line))
        result.append(aux)  
    final.extend(result.pop())
    for l in result:
        final = merge(l, final)
    return final      


if __name__ == '__main__':
    import doctest
    doctest.testmod()


