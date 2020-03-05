#!/bin/python

"""
Find a duplicate
We have a list of integers, where:
The integers are in the range 1..n1..n
The list has a length of n+1n+1
It follows that our list has at least one integer which appears at least twice. But it may have several duplicates, and each duplicate may appear more than twice.

Write a function which finds an integer that appears more than once in our list. (If there are multiple duplicates, you only need to find one of them.)
"""

def find_dups(num_list):
    num_dict = {}
    for n in num_list:
        if n in num_dict.keys():
            num_dict[n] += 1
        else:
            num_dict[n] = 1
    
    for k,v in num_dict.items():
        if v > 1:
            print "dup is {}".format(k)

def find_dups_set(num_list):
    
    num_set = set()

    for n in num_list:
        if n in num_set:
            print n
        else:
            num_set.add(n)


num_list = [6,1,3,7,6,4,5,2,8,5,6,6,7]
find_dups(num_list)
find_dups_set(num_list)
