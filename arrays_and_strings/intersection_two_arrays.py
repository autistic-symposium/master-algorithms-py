#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
        
  result = []
  set_nums = set(nums1) & set(nums2)
  counter = Counter(nums1) & Counter(nums2)
        
  for n in set_nums:
    result.extend([n] * counter[n])
        
  return result
        
