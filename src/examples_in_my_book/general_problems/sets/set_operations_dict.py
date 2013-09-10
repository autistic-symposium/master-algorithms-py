#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

from collections import OrderedDict

def  set_operations_with_dict():
    ''' find common in 2 dictionaries '''
    ''' values() do not support set operations!'''
    
    pairs = [('a', 1), ('b',2), ('c',3)]
    d1 = OrderedDict(pairs)
    print(d1)   # ('a', 1), ('b', 2), ('c', 3)
    
    d2 = {'a':1, 'c':2, 'd':3, 'e':4}
    print(d2)   # {'a': 1, 'c': 2, 'e': 4, 'd': 3}
    
    union = d1.keys() & d2.keys()
    print(union)    # {'a', 'c'}
    
    union_items = d1.items() & d2.items()
    print(union_items)  # {('a', 1)}
    
    subtraction1 = d1.keys() - d2.keys()
    print(subtraction1)  # {'b'}
    
    subtraction2 = d2.keys() - d1.keys()
    print(subtraction2)  # {'d', 'e'}
    
    subtraction_items = d1.items() - d2.items()
    print(subtraction_items)  # {('b', 2), ('c', 3)}

    ''' we can remove keys from a dict doing: '''
    d3 = {key:d2[key] for key in d2.keys() - {'c', 'd'}}
    print(d3) {'a': 1, 'e': 4}

if __name__ == '__main__':
    set_operations_with_dict()

