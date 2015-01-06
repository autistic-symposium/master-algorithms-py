#!/usr/bin/env python

__author__ = "bt3"


""" find whether two words are anagrams. Since sets do not count occurency, and sorting is O(nlogn)
we will use hash tables. We scan the first string and add all the character occurences. Then we
scan the second tring and decrease all the caracther occurences. If all the counts are zero, it is
an anagram"""

import string


def verify_two_strings_are_anagrams(str1, str2):
    ana_table = {key:0 for key in string.ascii_lowercase}

    for i in str1:
        ana_table[i] += 1

    for i in str2:
        ana_table[i] -= 1

    if len(set(ana_table.values())) < 2: return True
    else: return  False




''' verify if words are anagrams by comparying hash functions'''

def hash_func(astring, tablesize):
    sump = 0
    for p in astring:
        sump += ord(p)
    return sump%tablesize


def find_anagram_hash_function(word1, word2):
    tablesize = 11
    return hash_func(word1, tablesize) == hash_func(word2, tablesize)




if __name__ == '__main__':
    str1 = 'marina'
    str2 = 'aniram'
    str3 = 'anfaam'

    print verify_two_strings_are_anagrams(str1, str2)
    print verify_two_strings_are_anagrams(str1, str3)
    print
    print find_anagram_hash_function(str1, str2)
    print find_anagram_hash_function(str1, str3)


