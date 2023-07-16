#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


def merge_sort(array):
    """Sort an array using merge sort"""

    # part 1: recursively divide the array into subarrays
    if len(array) < 2:
        return array
    
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    # part 2: merge the subarrays
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1
    
    if left[i:]:
        result.extend(left[i:])
    if right[j:]:
        result.extend(right[j:])
    
    return result


def quick_sort_partition(array):
    """Sort an array using quick sort"""

    pivot, array = array[0], array[1:]

    lower = [i for i in array if i <= pivot]
    higher = [i for i in array if i > pivot]

    return lower, pivot, higher

def quick_sort_divided(array):
    """Sort an array using quick sort"""

    if len(array) < 2:
        return array

    lower, pivot, higher = quick_sort_partition(array)
    return quick_sort_divided(lower) + [pivot] + quick_sort_divided(higher)


if __name__ == '__main__':

    array = [3, 5, 1, 2, 10, 6]
    print(f'Array: {array}')

    print(f'Testing merge sort: {merge_sort(array)}')
    print(f'Testing quick sort: {quick_sort_divided(array)}')
