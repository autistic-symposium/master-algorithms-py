#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

''' reverse words in a setence, keeping the words right 
   >>> str1 = 'I love Google and Python!'
   >>> reverse_words(str1)
   'Python! and Google love I'
   >>> reverse_words('bla')
   'bla'
   >>> reverse_words('')
   ''
   >>> reverse_words_brute(str1)
   'Python! and Google love I'
   >>> reverse_words_brute('bla')
   'bla'
   >>> reverse_words_brute('')
   ''
'''

def reverse_words(str1):
    l1 = str1.split(' ')
    l1.reverse()
    return ' '.join(l1)
    
def reverse_words_brute(str1):
    aux_lt = []
    aux_str = ''
    for i, c in enumerate(str1):
        if c != ' ':
            aux_str += c    # WE COULD HAVE USED LT HERE, MORE EFFICIENT
        elif c == ' ':
            aux_lt.append(aux_str)  # WE COULD HAVE USED STR BUT NOT EFFICIENT!
            aux_str = ''
    aux_lt.append(aux_str) # REMEMBER THAT THE LAST ONE DOEN'T HAVE SPACE!
    aux_lt.reverse()   
    return ' '.join(aux_lt)

    

if __name__ == '__main__':
    import doctest
    doctest.testmod()

