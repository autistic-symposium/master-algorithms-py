#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

import string


def verify_two_strings_are_anagrams(str1, str2):
    """ find whether two words are anagrams. Since sets do not count occurency, and sorting is O(nlogn) 
    we will use hash tables. We scan the first string and add all the character occurences. Then we
    scan the second tring and decrease all the caracther occurences. If all the counts are zero, it is 
    an anagram"""
    
    # create the hash table
    ana_table = {key:0 for key in string.ascii_lowercase}
    
    # scan first string
    for i in str1:
        ana_table[i] += 1
     
    # scan second string
    for i in str2:
        ana_table[i] -= 1
    
    # verify whether all the entries are 0
    if len(set(ana_table.values())) < 2: return True
    else: return  False


def test_verify_two_strings_are_anagrams():
    str1 = 'marina'
    str2 = 'aniram'
    assert(verify_two_strings_are_anagrams(str1, str2) == True)
    str1 = 'google'
    str2 = 'gouglo'
    assert(verify_two_strings_are_anagrams(str1, str2) == False)
    print('Tests passed!')


if __name__ == '__main__':
    test_verify_two_strings_are_anagrams()




