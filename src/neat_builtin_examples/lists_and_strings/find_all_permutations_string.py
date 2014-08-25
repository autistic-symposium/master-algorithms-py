#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail



def find_all_permutations_string(str1):
    ''' print all the permutations of a given string, recursive so runtime is O(n*(n-1)) '''
    res = []
    if len(str1) == 1:
        res = [str1]
    else:
        for i, c in enumerate(str1):
            for perm in find_all_permutations_string(str1[:i] + str1[i+1:]):
                res += [c + perm]
    return res


def find_all_permutations_string_crazy(str1):
    ''' crazy simple way of find all the permutations of a string, also using recursion'''
    return [str1] if len(str1) == 1 else [c + perm for i, c in enumerate(str1) for perm in find_all_permutations_string_crazy(str1[:i]+str1[i+1:])]


def find_all_permutations_string_stdlib(str1):
    ''' find all the permutations of a string just using the available packages '''
    from itertools import permutations
    perms = [''.join(p) for p in permutations(str1)]
    return perms


def test_find_all_permutations_string():
    str1 = "abc"
    perm_set = {'abc', 'bac', 'cab', 'acb', 'cba', 'bca'}
    assert(set(find_all_permutations_string(str1)) == perm_set)
    assert(set(find_all_permutations_string_crazy(str1)) == perm_set)
    assert(set(find_all_permutations_string_stdlib(str1)) == perm_set)
    print('Tests passed!')


if __name__ == '__main__':
    test_find_all_permutations_string()





  
