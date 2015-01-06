#!/usr/bin/python

__author__ = "bt3"


''' find the lowest ancestor in a BST '''

from transversal_BST_recursively import BSTwithTransversalRecursively



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
        else:
            return None # this is probably never touched




if __name__ == '__main__':
    bst = BSTwithTransversalRecursively()
    l = [10, 5, 15, 1, 6, 11, 50]
    for i in l:
        bst.addNode(i)
    path = bst.preorder()
    print("The path inorder: ", path)

    print("The path between 1 and 6 is :", find_ancestor(path, 1, 6))
    print("The path between 1 and 11 is: ", find_ancestor(path, 1, 11))
    print("The path between 11 and 50 is: ", find_ancestor(path, 11, 50))
    print("The path between 5 and 15 is: ", find_ancestor(path, 5, 15))
