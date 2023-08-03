#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

def insertion_sort(lst):

        for i in range(1, len(lst)):
            current_index = i

            while current_index > 0 and lst[current_index - 1] > lst[current_index]:

                lst[current_index], lst[current_index - 1] = lst[current_index - 1], lst[current_index]
                current_index -= 1
