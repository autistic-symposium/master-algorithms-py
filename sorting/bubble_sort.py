#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def bubble_sort(array)

        has_swapped = True
  
        while has_swapped:
            has_swapped = False
          
            for i in range(len(array) - 1):
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    has_swapped = True          
