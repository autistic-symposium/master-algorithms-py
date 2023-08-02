#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


def heap_sort(self, lst: List[int]) -> None:

      def max_heapify(heap_size, index):
        
            left, right = 2 * index + 1, 2 * index + 2
            largest = index
        
            if left < heap_size and lst[left] > lst[largest]:
                largest = left
            if right < heap_size and lst[right] > lst[largest]:
                largest = right
            if largest != index:
                lst[index], lst[largest] = lst[largest], lst[index]
                max_heapify(heap_size, largest)

      for i in range(len(lst) // 2 - 1, -1, -1):
            max_heapify(len(lst), i)

      for i in range(len(lst) - 1, 0, -1):
            lst[i], lst[0] = lst[0], lst[i]
            max_heapify(i, 0)
        
