#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail


def hash_func(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])
    return sum%tablesize


def find_anagram_hash_function(word1, word2):
    ''' verify if words are anagrams by comparying hash functions'''
    tablesize = 11
    return hash_func(word1, tablesize) == hash_func(word2, tablesize)
   



def test_find_anagram_hash_function(module_name='this module'):
    word1 = 'buffy'
    word2 = 'bffyu'
    word3 = 'bffya'
    assert(find_anagram_hash_function(word1, word2) == True)
    assert(find_anagram_hash_function(word1, word3) == False)   
         
    s = 'Tests in {name} have {con}!'
    print(s.format(name=module_name, con='passed'))


if __name__ == '__main__':
    test_find_anagram_hash_function()

