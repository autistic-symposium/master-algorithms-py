#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

''' remove the chars in a list from a string
   ---> handle whitespaces!!!!
   >>> remove_char_str('I love google', 'oe')
   'I lv ggl'
   >>> remove_char_str('google', '')
   'google'
   >>> remove_char_str('google', 'google')
   ''
'''


def  remove_char_str(s1, charlist):
    set_aux = set(charlist)
    lt_aux = [] # we use list intead of concat. strs because it's more efficient
    for c in s1:
        if c not in set_aux:
            lt_aux.append(c)
    return ''.join(lt_aux)      # IF NON CHARS, RETURN '' not NONE!

    

if __name__ == '__main__':
    import doctest
    doctest.testmod()

