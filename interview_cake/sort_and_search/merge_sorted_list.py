#!/usr/bin/env python

"""
In order to win the prize for most cookies sold, my friend Alice and 
# I are going to merge our Girl Scout Cookies orders and enter as one unit.
# Each order is represented by an "order id" (an integer).
We have our lists of orders sorted numerically already, in lists. 
Write a function to merge our lists of orders into one sorted list.
"""

def merge_lists(my_list, alices_list):

    result = []
    index_alice_list = 0
    index_my_list = 0

    while index_alice_list < len(alices_list) and index_my_list < len(my_list):
        if alices_list[index_alice_list] < my_list[index_my_list]:
            result.append(alices_list[index_alice_list])
            index_alice_list += 1
        elif alices_list[index_alice_list] > my_list[index_my_list]:
            result.append(my_list[index_my_list])
            index_my_list += 1
        else:
            result.append(my_list[index_my_list])
            result.append(alices_list[index_alice_list])
            index_my_list += 1
            index_alice_list += 1
    
    if index_alice_list < len(alices_list):
        result.extend(alices_list[index_alice_list:])
    
    if index_my_list < len(my_list):
        result.extend(my_list[index_my_list:])
            
    return result


my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]


print merge_lists(my_list, alices_list)
print "Must be [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]"


# Or just using Timsort
def merge_sorted_lists(arr1, arr2):
    return sorted(arr1 + arr2)

print merge_sorted_lists(my_list, alices_list)
print "Must be [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]"