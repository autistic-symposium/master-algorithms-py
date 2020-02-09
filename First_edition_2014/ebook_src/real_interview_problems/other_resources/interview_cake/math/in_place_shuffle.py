#!/bin/python

"""
Write a function for doing an in-place shuffle of a list.

The shuffle must be "uniform," meaning each item in the original list must have the same probability of ending up in each spot in the final list.

Assume that you have a function get_random(floor, ceiling) for getting a random integer that is >= floor and <= ceiling.
"""

import random

def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)

def shuffle(the_list):

    if len(the_list) <= 1:
        return the_list

    last_index_in_the_list = len(the_list) - 1

    for i in range(len(the_list) - 1):
        random_choice_index = get_random(i,
                                         last_index_in_the_list)
        if random_choice_index != i:
            the_list[i], the_list[random_choice_index] = \
                the_list[random_choice_index], the_list[i]


seed_list = [5, 2, 6, 2, 6]
shuffle(seed_list)
print seed_list