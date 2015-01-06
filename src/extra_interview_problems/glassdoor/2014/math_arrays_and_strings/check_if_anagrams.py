#!/usr/bin/env python

__author__ = "bt3"


""" find whether two words are anagrams. Since sets do not count occurrence,
and sorting is O(nlogn) we will use hash tables. We scan the first string
and add all the character occurrences. Then we scan the second trying and
decrease all the character occurrences. If all the counts are zero, it is
an anagram"""

from collections import Counter

def verify_two_strings_are_anagrams(str1, str2):

    ana_table = Counter()

    for i in str1:
        ana_table[i] += 1

    for i in str2:
        ana_table[i] -= 1

    if len(set(ana_table.values())) < 2:
        return True
    else:
        return  False


''' verify if words are anagrams by comparing a sum of  Unicode code
point of the character'''

def get_unicode_sum(word):
    s = 0
    for p in word:
        s += ord(p)
    return s


def find_anagram_get_unicode(word1, word2):
    return get_unicode_sum(word1) == get_unicode_sum(word2)




if __name__ == '__main__':
    str1 = 'marina'
    str2 = 'aniram'
    str3 = 'anfaam'

    assert(verify_two_strings_are_anagrams(str1, str2) == True)
    assert(verify_two_strings_are_anagrams(str1, str3) == False)

    assert(find_anagram_get_unicode(str1, str2) == True)
    assert(find_anagram_get_unicode(str1, str3) == False)
