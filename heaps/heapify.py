#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

# python's built-in heap differs from the standard implementation of a heap
# in two ways. firstly, it uses zero-based indexing, so it stores the root
# node at index zero instead of the size of the heap. secondly, the built-in
# module does not offer a direct way to create a max heap, instead, we must
# modify the values of each eelement when inserting in the heap, and when
# removing it from the heap.

import heapq

min_heap = [3,1,2]
heapq.heapify(min_heap)

max_heap = [-x for x in min_heap]
heapq.heapify(max_heap)

heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, -5)

min_elem = min_heap[0]
max_elem = -1 * max_heap[0

heapq.heappop(min_heap)
heapq.heappop(max_heap)

size_min_heap = len(min_heap)
size_max_heap = len(max_heap)
