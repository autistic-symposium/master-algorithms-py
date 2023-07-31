#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


def find_min(nums):
        
        left, right = 0, len(nums) - 1
        
        while nums[left] > nums[right]:
            
            mid = (left + right) // 2
            
            if nums[mid] < nums[right]:
                # note above that it's on right
                right = mid
            else:
                left =  mid + 1
                
        return nums[left]
  
