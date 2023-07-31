#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

def top_k_frequentnums: list[int], k: int) -> list[int]:
        
  # O(1) time
  if k == len(nums):
    return nums

  # 1. build a hashmap element: frequency
  counter = Counter(nums)

  # 2. build a heap of k most frequent elements
  # 3. build an output array
  # O(N log k) time
  return heapq.nlargest(k, counter.keys(), key=counter.get)
