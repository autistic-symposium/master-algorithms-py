#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

''' find the first non-repetead char in a str.
   ---> we use a dict to count occurences
   >>> find_non_rep_char("cut")
   'c'
   >>> s1 = 'google'
   >>> find_non_rep_char(s1)
   'l'
   >>> find_non_rep_char('ccc')
   >>> find_non_rep_char('')
'''

from collections import Counter
def  find_non_rep_char(s1):
    aux_dict = Counter()
    for i in s1:
        aux_dict[i] += 1
    for i in s1:
        if aux_dict[i] < 2: return i  # remember it's <2
    # not handling anything else: return None

    

if __name__ == '__main__':
    import doctest
    doctest.testmod()

