#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

import string

def delete_unique_word(str1):
    '''  find and delete all the duplicate characters in a string '''

    # create ordered dict
    table_c = { key : 0  for key in string.ascii_lowercase}
    
    # fill the table with the chars in the string
    for i in str1:
        table_c[i] += 1
    
    # scan the table to find times chars > 1
    for key, value in table_c.items():
        if value > 1:
            str1 = str1.replace(key, "")
          
    return str1


def test_delete_unique_word():
    str1 = "google"
    assert(delete_unique_word(str1) == 'le')
    print('Tests passed!')

if __name__ == '__main__':
    test_delete_unique_word()

