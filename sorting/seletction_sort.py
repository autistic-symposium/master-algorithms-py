#!/usr/bin/env python3
# -*- coding: utf-8 -*-



def selection_sort(array):

    for i in range(len(array)):
        min_index = i
        
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

    array[min_index], array[i] = array[i], array[min_index]
