#!/bin/python

'''
Given a tree find out whether is a BST or not
'''

class Tree(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def create_tree_bst():
    tree = Tree(4)
    tree.right = Tree(6)
    tree.left = Tree(2)
    tree.right.left = Tree(5)
    tree.right.right = Tree(7)
    tree.left.left = Tree(1)
    tree.left.right = Tree(3)
    return tree

def create_tree_not_bst():
    tree = Tree(4)
    tree.right = Tree(6)
    tree.left = Tree(2)
    tree.right.left = Tree(5)
    tree.right.right = Tree(7)
    tree.left.left = Tree(3)
    tree.left.right = Tree(1)
    return tree


INFINITY = float("infinity")
NEG_INFINITY = float("-infinity")

def isBST(tree, minVal=NEG_INFINITY, maxVal=INFINITY):
    if not tree:
        return True

    if not minVal <= tree.value <= maxVal:
        return False

    return isBST(tree.left, minVal, tree.value) and \
           isBST(tree.right, tree.value, maxVal)


if __name__ == '__main__':
    tree = create_tree_bst()
    print isBST(tree)

    tree = create_tree_not_bst()
    print isBST(tree)
