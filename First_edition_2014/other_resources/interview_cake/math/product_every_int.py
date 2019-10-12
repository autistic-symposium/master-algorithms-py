#!/bin/python

"""
You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.

Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]
 
by calculating:

  [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]
 
Here's the catch: You can't use division in your solution!
"""

def get_products_of_all_ints_except_at_index(array):
    prod_array = []

    for i, num in enumerate(array):
        prod = 1
        for other_num in array[:i] + array[i+1:]:
            prod *= other_num
            
        prod_array.append(prod)

    return prod_array


array = [1, 7, 3, 4]
print get_products_of_all_ints_except_at_index(array)
print "Should be [84, 12, 28, 21]"