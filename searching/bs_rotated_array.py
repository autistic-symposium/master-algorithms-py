#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


def search(nums):
        
        # 1. find the smallest element in the rotate array
        # "left" will be used as index later
        
        left, right = 0, len(nums)
        while left < right:

            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid
        
        
        # 2. write a binary search
        def bs(left, right, target):

            while left <= right:

                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid
                
                elif nums[mid] > target:
                    right = mid - 1
                
                else:
                    left = mid + 1
            
            return -1
        
        # 3. run for both sides
        response = bs(0, left, target) 
        if response != -1:
            return response
        
        else:
            return bs(left, len(nums), target)
          
