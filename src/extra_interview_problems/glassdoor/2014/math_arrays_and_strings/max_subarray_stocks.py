#!/usr/bin/env python

__author__ = "bt3"



def beating_stock(array):

    imin = 0
    i = 1
    deal = [array[i] - array[imin], imin, i]

    while i < len(array):

        deal_here = array[i] - array[imin]
        if deal_here > deal[0]:
            deal = [deal_here, imin, i]

        elif array[i] < array[imin]:
            imin = i

        i += 1

    return deal[0], array[deal[1]], array[deal[2]]










array = [7, 2, 3, 6, 5, 8, 5, 3, 4]
print(array)
print("The best profit is %d, buying at %d, selling at %d." %(beating_stock(array)))