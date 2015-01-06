#!/bin/python

'''
Reconstruct a binary tree given two sequences of node traversals,
one from inorder and one from postorder traversal.
'''

class Node(object):
    def __init__(self, value, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left

def create_tree():
    tree = Node(4)
    tree.right = Node(6)
    tree.left = Node(2)
    tree.right.left = Node(5)
    tree.right.right = Node(7)
    tree.left.left = Node(1)
    tree.left.right = Node(3)
    return tree

def inorder(tree):
    if tree:
        if tree.left:
            inorder(tree.left)
        print tree.value
        if tree.right:
            inorder(tree.right)

def postorder(tree):
    if tree:
        if tree.left:
            postorder(tree.left)
        if tree.right:
            postorder(tree.right)
        print tree.value





if __name__ == '__main__':
    tree = create_tree()
    print 'Printing inorder...'
    inorder(tree)
    print
    print 'Printing postorder...'
    postorder(tree)
