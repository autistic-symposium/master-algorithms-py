#!/bin/python

''' Quick sort an array '''


def quick_sort(arr):
    if len(arr) < 2: return arr
    piv = len(arr)//2
    left = [x for i, x in enumerate(arr) if x <= arr[piv] and i != piv]
    right = [x for i, x in enumerate(arr) if x > arr[piv] and i != piv]
    return quick_sort(left) + [arr[piv]] + quick_sort(right)



if __name__ == '__main__':
    arr = [8, 5, 2, 6, 1, 2, 9, 4]
    print(quick_sort(arr))