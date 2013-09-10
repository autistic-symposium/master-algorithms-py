#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

   
def unique_char(s):
    if len(s) > 256: return False
    set_chars = set()
    for i in s:
        if i in set_chars:
            return False
        else:
            set_chars.add(i) 
    return True
    
    
    
def unique_char_no_add(s):
    if len(s) < 2: return True
    for i, c in enumerate(s):
        for j in s[i+1:]:
            if j == c:
                return False
    return True
    

def main():
    s1 = 'abcdefg'
    s2 = 'buffy'
    s3 = ''
    print(unique_char(s1))
    print(unique_char(s2))
    print(unique_char(s3))
    print(unique_char_no_add(s1) )
    print(unique_char_no_add(s2))
    print(unique_char_no_add(s3))
    
                   
if __name__ == '__main__':
    main()

