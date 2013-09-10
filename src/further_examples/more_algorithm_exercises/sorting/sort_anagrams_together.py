#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

''' A method to sort an array so that all the anagrams are together. Since we only
    want the anagrams to be grouped, we can use a dictionary for this task. This
    algorithm is O(n).
    >>> l1 = ['hat', 'ball', 'tha', 'cut', 'labl', 'hta', 'cool', 'cuy', 'uct']
    >>> sort_anagrams_together(l1)
    ['cut', 'uct', 'cool', 'ball', 'labl', 'hat', 'tha', 'hta', 'cuy']
'''

from collections import defaultdict
def sort_anagrams_together(l1):
    result = []
    
    # step 1 save the anagrams together
    dict_aux = defaultdict(list) # rememebr to indicate the type
    for word in l1:
        key = ''.join(sorted(word)) # need to sort the strings and join it
        dict_aux[key].append(word) # because only sorted give a list of each char
    
    # step 2 print the anagrams. Note that if you want everything
    # sorted you would have to sort the keys and insert the angrams after that    
    for key in dict_aux:
        result.extend(dict_aux[key])
        
    return result
    
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()

