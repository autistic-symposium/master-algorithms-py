#!/usr/bin/python


def find_permutations(s):
    if len(s) < 2: return s
    res = []
    for i, c in enumerate(s):
        for perm in find_permutations(s[:i] + s[i+1:]):
            res.append(c + "".join(perm))
    return res


def fpc(s):
    return [s] if len(s)<2 else [c+p for i,c in enumerate(s) for p in fpc(s[:i]+s[i+1:])]


def find_permutations_stdlib(s):
    from itertools import permutations
    return [''.join(p) for p in permutations(s)]


def find_permutations2(s):
    if len(s) < 2: return s
    res = []
    for i in range(len(s)):
        for perm in find_permutations2(s[:i] + s[i+1:]):
            res.append(s[i] + perm)
    return res


def verify_if_perm(s1, s2):
    if len(s1) != len(s2): return False
    s1 = sorted(s1)
    s2 = sorted(s2)
    return s1 == s2


from collections import Counter
def verify_if_perm2(s1, s2): # like anagram
    if len(s1) != len(s2): return False
    dict_aux = Counter()
    for c in s1:
        dict_aux[c] += 1
    for c in s2:
        dict_aux[c] -= 1
    for item in dict_aux:
        if dict_aux[item]:
            return False
    return True



if __name__ == '__main__':
    s1 = 'ufyfbufyfb'
    s2 = 'buffybuffy'
    s3 = 'uuyfbuuyfb'
    s4 = ''

    print(verify_if_perm(s1, s2))
    print(verify_if_perm(s1, s3))
    print(verify_if_perm(s1, s4))
    print
    print(verify_if_perm2(s1, s2))
    print(verify_if_perm2(s1, s3))
    print(verify_if_perm2(s1, s4))

    print

    s = 'hat'
    print find_permutations(s)
    print fpc(s)
    print find_permutations_stdlib(s)
    print find_permutations2(s)
    print
    print find_permutations(s4)
    print fpc(s4)
    print find_permutations_stdlib(s4)
    print find_permutations2(s4)



