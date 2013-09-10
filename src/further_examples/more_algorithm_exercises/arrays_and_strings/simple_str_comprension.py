#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

   
from collections import Counter
def str_comp(s):
    ''' basic str compression with counts of repeated char'''
    count, last = 1, ''
    list_aux = []
    for i, c in enumerate(s):
        if last == c:
            count += 1
        else:
            if i != 0:
                list_aux.append(str(count))
            list_aux.append(c)
            count = 1
            last = c
    list_aux.append(str(count))    
    return ''.join(list_aux)
        

def main():
    s1 = 'aabcccccaaa'
    s2 = ''
    print(str_comp(s1)) # 'a2b1c5a3'
    print(str_comp(s2))
                   
if __name__ == '__main__':
    main()

