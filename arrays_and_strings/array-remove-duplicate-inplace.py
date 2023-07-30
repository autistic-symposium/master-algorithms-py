#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

### Remove Duplicates from Sorted Array in-place


def remove_duplicates(nums: list[int]) -> int:
        
        arr_i, dup_i = 0, 1
        
        while arr_i < len(nums) and dup_i < len(nums):
        
            if nums[arr_i] == nums[dup_i]:
                dup_i += 1

            else:
                arr_i += 1
                nums[arr_i] = nums[dup_i]
        
        for i in range(arr_i + 1, dup_i):
            nums[i] = '_'
        
        return  dup_i - arr_i - 1, nums
            


if __name__ == "__main__":


    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert(remove_duplicates(nums) == (5, [0, 1, 2, 3, 4, '_', '_', '_', '_', '_']))
