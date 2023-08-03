#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


def counting_sort(list):

        K = max(lst)
        counts = [0] * (K + 1)
        for elem in lst:
            counts[elem] += 1

        starting_index = 0
        for i, count in enumerate(counts):
            counts[i] = starting_index
            starting_index += count

        sorted_lst = [0] * len(lst)

        for elem in lst:

            sorted_lst[counts[elem]] = elem
            counts[elem] += 1

        for i in range(len(lst)):
            lst[i] = sorted_lst[i]
