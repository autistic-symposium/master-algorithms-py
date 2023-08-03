#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


def selection_sort(lst):

    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j

    lst[min_index], lst[i] = lst[i], lst[min_index]
