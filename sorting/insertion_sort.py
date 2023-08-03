#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def insertion_sort(array):

        for i in range(1, len(array)):
            current_index = i

            while current_index > 0 and array[current_index - 1] > array[current_index]:

                array[current_index], array[current_index - 1] = array[current_index - 1], array[current_index]
                current_index -= 1
