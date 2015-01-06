#!/usr/bin/env python

__author__ = "bt3"

"""
Given an integer x and an unsorted array of integers, describe an algorithm to
determine whether two of the numbers add up to x.

1. Using hash tables.
2. Sorting the array and keeping two pointers in the array, one in the beginning and
one in the end. Whenever the sum of the current two integers is less than x, move the
first pointer forwards, and whenever the sum is greater than x, move the second pointer
backwards. O(nln n).
3. Create a BST with x minus each element in the array. Check whether any element of
the array appears in the BST. It takes O(nlog n) times two.
"""


def check_if_sum(arr, num):
    seq =  sorted(arr)
    p1, p2 = 0, len(arr) - 1
    while p1 < p2 and p2 < len(arr) and p1 >= 0:
        sum_here = seq[p1] + seq[p2]
        if sum_here == num:
            return True, seq[p1], seq[p2]
        elif sum_here < num:
            p1 += 1
        elif sum_here > num:
            p2 -= 1
    return False


from collections import Counter
def check_if_sum2(arr, num):
    d = Counter()
    for i in arr:
        d[i] += 1

    for i in arr:
        other = num - i
        d[i] -= 1
        if d[other] == 1:
            return True, other, i
    return False


arr = [3, 1, 13, 7, 2, 10]
num1 = 11
num2 = 6

print(check_if_sum(arr, num1))
print(check_if_sum(arr, num2))
print
print(check_if_sum2(arr, num1))
print(check_if_sum2(arr, num2))