#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

   
def ver_perm(s1, s2):
    ''' worst case O(nlogn + mlogm) = O(NlogN) '''
    if len(s1) != len(s2): return False
    s1 = sorted(s1)
    s2 = sorted(s2)
    return s1 == s2

from collections import Counter
def ver_perm_dict(s1, s2):
    ''' worst case O(n + n +2n) = O(n)'''
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

import time
def main():
    s1 = 'ufyfbufyfb'
    s2 = 'buffybuffy'
    s3 = 'uuyfbuuyfb'
    s4 = ''
    start = time.time()
    print(ver_perm(s1, s2))
    print(ver_perm(s1, s3))
    print(ver_perm(s1, s4))
    final1 = time.time() - start
    
    start = time.time()
    print(ver_perm_dict(s1, s2))
    print(ver_perm_dict(s1, s3))
    print(ver_perm_dict(s1, s4))
    final2 = time.time() - start
    
    print(final2-final1)
                      
if __name__ == '__main__':
    main()

