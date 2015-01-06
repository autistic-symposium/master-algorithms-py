#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

''' Find if a s2 is a substring of a s1
    >>> s1 = 'buffy is a vampire slayer'
    >>> s2 = 'vampire'
    >>> s3 = 'angel'
    >>> isSubstr(s1, s2)
    True
    >>> isSubstr(s1, s3)
    False
    >>> s4 = 'pirevam'
    >>> find_substr(s2, s4)
    True
    >>> find_substr(s1, s4)
    False
'''

def isSubstr(s1, s2):
    if s1 in s2 or s2 in s1: return True
    return False

   
def find_substr(s1, s2):
    if s1 == '' or s2 == '': return True #empty str is always substr
    for i, c in enumerate(s1):
        if c == s2[0]:
            test_s1 = s1[i:]+s1[:i]
            return isSubstr(s2, test_s1)
    return False


                   
if __name__ == '__main__':
    import doctest
    doctest.testmod()

