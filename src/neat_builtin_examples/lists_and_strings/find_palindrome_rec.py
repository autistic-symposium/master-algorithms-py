#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail


def find_palindrome_rec(s):
    ''' recursive way of checking whether a str is a palindrome '''
    if len(s) > 1: 
        if s[0] != s[-1]: return False
        else: find_palindrome_rec(s[1:-1])  
    return True


def test_find_palindrome_rec(module_name='this module'):
    str1 = 'radar'
    str2 = ""
    str3 = 'x'
    str4 = 'hello'
    assert(find_palindrome_rec(str1) == True)
    assert(find_palindrome_rec(str2) == True)
    assert(find_palindrome_rec(str3) == True)
    assert(find_palindrome_rec(str4) == False)       
    s = 'Tests in {name} have {con}!'
    print(s.format(name=module_name, con='passed'))


if __name__ == '__main__':
    test_find_palindrome_rec()

