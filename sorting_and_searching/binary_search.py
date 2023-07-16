#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

def binary_search_recursive(array, item, higher=None, lower=0):

    higher = higher or len(array)
    if higher < lower:
        return False
    
    mid = (higher + lower)//2
    if  item == array[mid]:
        return mid
    elif item < array[mid]:
        return binary_search_recursive(array, item, higher=mid-1, lower=lower)
    else:
        return binary_search_recursive(array, item, higher=higher, lower=mid+1)


def binary_search_iterative(array, item):
    lower, higher = 0, len(array)

    while lower < higher:
        mid = (higher+lower)//2
        if array[mid] == item:
            return mid
        elif array[mid] > item:
            higher = mid
        else:
            lower=mid+1
    return False


if __name__ == '__main__':

    array = [2, 3, 5, 6, 8, 10, 15, 23]
    item = 15
    
    print('Recursive: ', binary_search_recursive(array, item))
    print('Iterative: ', binary_search_iterative(array, item))
