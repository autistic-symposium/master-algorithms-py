#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


class SimpleTree:
    """Implementation of a simple tree"""

    def __init__(self, value=None, node=None):
        self.value = value
        self.node = node or []
        
    def __repr__(self, level=0):
        repr = '\t' * level  + self.value + '\n'
        for n in self.node:
            repr += n.__repr__(level + 1)
        return repr


class Node():
    """Implementation of a Node for a binary tree"""

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
    
    ############################
    #       Private Methods
    ############################
    def __repr__(self):
        """Prints the node"""
        return f'{self.value}'

    def _repr_preorder(self):
        """Prints the tree in preorder traversal (root, left, right)"""

        print(self.value)
        if self.left:
            self.left._repr_preorder()
        if self.right:
            self.right._repr_preorder()
    
    def _add_node_binary_tree(self, value):
        """Adds a node to a simple binary tree"""

        new_node = Node(value)
        if self.value is None:
            self.value = new_node
        
        else:
            if not self.left:
                self.left = new_node
            elif not self.right:
                self.right = new_node
            else:
                self.left = self.left._add_node_binary_tree(value)

        return self
    
    def _add_node_binary_search_tree(self, value) -> bool:
        """Adds a node to a binary search tree"""

        new_node = Node(value)
        if self.value is None:
            self.value = new_node

        else:
            if value < self.value:
                self.left = self.left and self.left._add_node_binary_search_tree(value) or new_node
            elif value > self.value:
                self.right = self.right and self.right._add_node_binary_search_tree(value) or new_node
            else:
                print("BSTs do not support repeated items.")
        
        return self

    def _search_node_preorder(self, value) -> bool:
        """Searches through preorder traversal (node, left, right)"""

        if self.value == value:
            return True
       
        found = False
        if self.left:
            # recursively search left
            found = self.left._search_node_preorder(value)
        
        if self.right:
            # recursively search right
            found = found or self.right._search_node_preorder(value)
        
        return found

    def _search_node_binary_search_tree(self, query) -> bool:
        """Searches the tree for a value, considering the BST property"""

        this_node_value = self.value

        if this_node_value is not None:
            print(this_node_value)
            if this_node_value == query:
                return True 

            elif this_node_value > query:
                if self.left is not None:
                    return self.left._search_node_binary_search_tree(query)

            elif this_node_value < query:
                if self.right is not None:
                    return self.right._search_node_binary_search_tree(query)
        
        return False
    
    def _isLeaf(self) -> bool:
        """If node has no children, it is a leaf"""

        return bool(not self.right and not self.left)
    
    def _isFull(self) -> bool:
        """If node has two children, it is full"""
        return bool(self.right and self.left)


class BinaryTreeInterface():

    def __init__(self):
        self.root = Node()

    ############################
    #       Interface Methods
    ############################
    def add_node(self, value):
        """Adds a new node to the tree"""
        pass

    def search_node(self, value):
        """Searches the tree for a value"""
        pass

    ############################
    #       Public Methods
    ############################
    def isLeaf(self) -> bool:
        """Returns True if the node is a leaf"""

        if self.root is not None:
            return self.root._isLeaf()

    def isFull(self) -> bool:
        """Returns True if the node is full"""

        if self.root is not None:
            return self.root._isFull()

    def print_preorder(self):
        """Prints the BST in preorder"""
        
        if self.root is not None:
            self.root._repr_preorder()


class BinaryTree(BinaryTreeInterface):
    """Implementation of a binary tree"""

    def add_node(self, value):
        """Adds a new node to the tree"""

        if self.root is None:
            self.root = Node(value)
        else:
            self.root._add_node_binary_tree(value)

    def search_node(self, value):
        """Searches the tree for a value"""

        if self.root:
            return self.root._search_node_preorder(value)


class BinarySearchTree(BinaryTreeInterface):
    
    def add_node(self, value):
        """Adds a new node to the tree"""

        if self.root is None:
            self.root = Node(value)
        else:
            self.root._add_node_binary_search_tree(value)

    def search_node(self, value):
        """Searches the tree for a value"""

        if self.root.value is not None:
            return self.root._search_node_binary_search_tree(value)




if __name__ == '__main__':

    ############################
    #   Test SimpleTree
    ############################
    print("\n\n   🌴 Testing SimpleTree 🌴")
    t = SimpleTree('a', [SimpleTree('b', [SimpleTree('d'), SimpleTree('e')]), \
                            SimpleTree('c', [SimpleTree('h'), SimpleTree('g')])])
    print(t)


    ############################
    #   Test binary tree
    ############################
    print("\n\n   🌳 Testing BinaryTree 🌳")
    bt = BinaryTree()
    print("\n   Adding nodes 1 to 10 in the tree...")
    for i in range(1, 11):
        bt.add_node(i)
    
    print("   Printing the tree in preorder...")   
    bt.print_preorder()

    print("\n   Searching for node 5...")
    print(bt.search_node(5))

    print("\n   Searching for node 15...")
    print(bt.search_node(15))

    print("\n   Checking if root is a leaf...")
    print(bt.isLeaf())

    print("\n   Checking if root is full...")
    print(bt.isFull())


    ##############################
    #   Test binary search tree
    ##############################
    print("\n\n   🎄 Testing BinarySearchTree 🎄")
    bst = BinarySearchTree()
    print("\n   Adding nodes 1 to 10 in the tree...")
    for i in range(1, 11):
        bst.add_node(i)
    
    print("   Printing the tree in preorder...")
    bst.print_preorder()

    print("\n   Searching for node 5...")
    print(bst.search_node(5))

    print("\n   Searching for node 15...")
    print(bst.search_node(15))

