#!/bin/python

"""
Given a list of integers, find the highest product you can get from three of the integers.

The input list_of_ints will always have at least three integers.
"""

def highest_num(list_of_ints):

    if len(list_of_ints) == 3:
        return list_of_ints[0]*list_of_ints[1]*list_of_ints[2]

    sorted_list = sorted(list_of_ints)

    return sorted_list[-3]*sorted_list[-2]*sorted_list[-1]


def highest_product_of_3_On(list_of_ints):

    highest = max(list_of_ints[0], list_of_ints[1])
    lowest  = min(list_of_ints[0], list_of_ints[1])
    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2  = list_of_ints[0] * list_of_ints[1]

    highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    for i in range(2, len(list_of_ints)):
        current = list_of_ints[i]

        highest_product_of_3 = max(highest_product_of_3,
                                   current * highest_product_of_2,
                                   current * lowest_product_of_2)

        highest_product_of_2 = max(highest_product_of_2,
                                   current * highest,
                                   current * lowest)

        lowest_product_of_2 = min(lowest_product_of_2,
                                  current * highest,
                                  current * lowest)

        highest = max(highest, current)

        lowest = min(lowest, current)

    return highest_product_of_3

list_of_ints = [4, 2, 5, 6]
print highest_num(list_of_ints)
print "Should be 120"

print highest_product_of_3_On(list_of_ints)
print "Should be 120"