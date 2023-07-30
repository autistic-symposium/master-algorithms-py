#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

'''
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
'''

def valid_mountain_array(arr: list[int]) -> bool:
        
        last_number, mountain_up = arr[0], True
        
        for i, n in enumerate(arr[1:]):
            
            if n > last_number:
                
                if mountain_up == False:
                    return False
                
            elif n < last_number:
                
                if i == 0:
                    return False
                mountain_up = False
            
            else:
                return False
            
            last_number = n
        
        return not mountain_up


if __name__ == "__main__":
    arr = [0,3,2,1]
    print(valid_mountain_array(arr))
