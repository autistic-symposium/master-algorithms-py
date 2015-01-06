#!/usr/bin/env python

__author__ = "bt3"


def isSubstr(s1, s2):
    if s1 in s2 or s2 in s1: return True
    return False


def find_substr(s1, s2):
    pl, ps = 0, 0
    if len(s1) > len(s2):
        larger, smaller = s1, s2
    else:
        larger, smaller = s2, s1
    while ps < len(smaller) and pl < len(larger):
        if larger[pl] == smaller[ps]:
            ps += 1
        else:
            ps = 0
        pl += 1
        if ps == len(smaller):
            return True
    return False



if __name__ == '__main__':
    s1 = 'buffy is a vampire slayer'
    s2 = 'vampire'
    s3 = 'angel'
    print find_substr(s2, s1)
    print find_substr(s3, s1)
