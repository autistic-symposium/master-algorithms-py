#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def counting_sort(array):

        k = max(array)
        counts = [0] * (k + 1)
        
        for e in array:
            counts[e] += 1

        starting_index = 0
        for i, count in enumerate(counts):
            counts[i] = starting_index
            starting_index += count

        sorted_list = [0] * len(array)

        for e in array:

            sorted_list[counts[e]] = e
            counts[e] += 1

        for i in range(len(array)):
            array[i] = sorted_list[i]
