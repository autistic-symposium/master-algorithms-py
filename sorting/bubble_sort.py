#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


def bubble_sort(list)

        has_swapped = True
  
        while has_swapped:
            has_swapped = False
          
            for i in range(len(lst) - 1):
                if lst[i] > lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    has_swapped = True          
