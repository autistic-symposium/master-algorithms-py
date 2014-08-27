#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

from BST_traversal import TranversalBST

def find_ancestor(path, low_value, high_value):
    ''' find the lowest ancestor in a BST '''       
    while path:
        current_value = path[0]
        if current_value < low_value:
            try:
                path = path[2:]
            except:
                return current_value
        elif current_value > high_value:
            try:
                path = path[1:]
            except:
                return current_value
        elif low_value <= current_value <= high_value:
            return current_value
    return None


def test_find_ancestor():
    """
            10 
       5       15
    1   6     11    50
    """     
    t = TranversalBST()
    l1 = [10, 5, 15, 1, 6, 11, 50]
    for i in l1: t.insert(i)
    path = t.preorder()
    assert(find_ancestor(path, 1, 6) == 5)
    assert(find_ancestor(path, 1, 11) == 10) 
    assert(find_ancestor(path, 11, 50) == 15)   
    assert(find_ancestor(path, 5, 15) == 10)  
    
    
    print("Tests passsed!")
    
if __name__ == '__main__':
    test_find_ancestor()

