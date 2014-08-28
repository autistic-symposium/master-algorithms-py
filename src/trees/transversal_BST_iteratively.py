#!/usr/bin/python

__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"


from collections import deque
from binary_search_tree import BinarySearchTree, NodeBST



class BSTwithTransversalIterative(BinarySearchTree):

    def inorder(self):
        current = self.root
        nodes, stack = [], []
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                nodes.append(current.item) # thats what change
                current = current.right
        return nodes


    def preorder(self):
        current = self.root
        nodes, stack = [], []
        while stack or current:
            if current:
                nodes.append(current.item) # thats what change
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                current = current.right
        return nodes


    def preorder2(self):
        nodes = []
        stack = [self.root]
        while stack:
            current = stack.pop()
            if current:
                nodes.append(current.item)
                stack.append(current.right)
                stack.append(current.left)
        return nodes


    def BFT(self):
        current = self.root
        nodes = []
        queue = deque()
        queue.append(current)
        while queue:
            current = queue.popleft()
            nodes.append(current.item)
            if current.left:
                queue.append(current.left) # LEFT FIRST!
            if current.right:
                queue.append(current.right)
        return nodes






if __name__ == '__main__':

    bst = BSTwithTransversalIterative()
    l = [10, 5, 6, 3, 8, 2, 1, 11, 9, 4]
    for i in l:
        bst.addNode(i)

    print "Is 8 a leaf? ", bst.isLeaf(8)
    print "Whats the level of node 8? ", bst.getNodeLevel(8)
    print "Is node 10 a root? ", bst.isRoot(10)
    print "Is node 1 a root? ", bst.isRoot(1)
    print "Whats the tree height? ", bst.getHeight()
    print "Is this tree BST? ", bst.isBST()
    print "Is this tree balanced? ", bst.isBalanced()

    print("Pre-order I: ", bst.preorder())
    print("Pre-order II: ", bst.preorder2())
    print("In-order: ", bst.inorder())
    print("BFT: ", bst.BFT())
