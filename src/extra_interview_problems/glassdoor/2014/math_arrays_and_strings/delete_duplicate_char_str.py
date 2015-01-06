#!/usr/bin/python

'''  find and delete all the duplicate characters in a string '''


import string

def delete_unique_word(str1):
    table_c = { key : 0  for key in string.ascii_lowercase}
    for i in str1:
        table_c[i] += 1
    for key, value in table_c.items():
        if value > 1:
            str1 = str1.replace(key, "")

    return str1



if __name__ == '__main__':
    str1 = "google"
    print delete_unique_word(str1) # == 'le'

