#!/usr/bin/env python

__author__ = "bt3"


from binary_search_tree import BST, Node
from transversal import inorder

def find_ancestor(path, low_value, high_value):

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


if __name__ == '__main__':


    bst = BST()
    l = [10, 5, 6, 3, 8, 2, 1, 11, 9, 4]
    for i in l:
        bst.add(i)
    nodes = inorder(bst.root)
    print 'Original:    ', l
    print 'Inorder:     ', nodes
    print 'Ancestor for 3, 11:', find_ancestor(nodes, 3, 11)
