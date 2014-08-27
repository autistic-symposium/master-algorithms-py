#!/usr/bin/python3
# mari von steinkirch 2013

from binary_tree import BinaryTree, NodeBT

''' Implementation of a binary search tree and its properties. 
    We use the Binary Tree class and its Node class as superclasses, and  we modify the methods
    that are needeed to create a BST (polymorphism). For example, the following bst:   
       
                              7                      ---> level 0
                   4                  9              ---> level 1
               2       5          8       10         ---> level 2
             1            6                          ---> level 3 
             
    has the following properties:
    
        - SIZE OR NUMBER OF NODES: n = 10
        - NUMBER OF BRANCHES OR INTERNAL NODES: b = n-1 = 9
        - VALUE OF ROOT = 7
        - MAX_DEPTH OR HEIGHT: h = 3
        - IS BALANCED? YES
        - IS BST? YES
        - INORDER DFT: 1, 2, 4, 5, 6, 7, 8, 9, 10
        - POSTORDER DFT: 1, 2, 6, 5, 4, 8, 10, 9, 7
        - PREORDER DFT: 7, 4, 2, 1, 5, 6, 9, 8, 10
        - BFT:  7, 4, 9, 2, 5, 8, 10, 1, 6
'''


class NodeBST(NodeBT):

    def _addNextNode(self, value, level_here=1):
        ''' Aux for self.addNode(value): for BST, best O(1), worst O(log n) '''
        self.traversal = []
        new_node = NodeBST(value, level_here)
        if not self.item:
            self.item = new_node
        elif value < self.item:  
            self.left = self.left and self.left._addNextNode(value, level_here+1) or new_node
        else:
            self.right = self.right and self.right._addNextNode(value, level_here+1) or new_node         
        return self 
     
    def _searchForNode(self, value):
        ''' Traverse the tree looking for the node. For BST it is O(logn) if the
            tree is balanced, otherwise it can be O(n) '''
        if self.item == value: return self
        elif value > self.item and self.right: return self.right._findNode(value)
        elif value < self.item and self.left: return self.left._findNode(value)
        return None


     
class BinarySearchTree(BinaryTree):
    '''     
    >>> bst = BinarySearchTree()
    >>> l1 = [7, 4, 5, 9, 2, 8, 1, 6, 10]
    >>> for i in l1: bst.addNode(i)
    >>> bst.hasNode(3)
    False
    >>> bst.hasNode(10)
    True
    >>> bst.printTree('pre')
    [7, 4, 2, 1, 5, 6, 9, 8, 10]
    >>> bst.printTree('post')
    [1, 2, 6, 5, 4, 8, 10, 9, 7]
    >>> bst.printTree('in')
    [1, 2, 4, 5, 6, 7, 8, 9, 10]
    >>> bst.printTree('bft')
    [7, 4, 9, 2, 5, 8, 10, 1, 6]
    >>> bst.getHeight()
    3
    >>> bst.isBST()
    True
    >>> bst.isBalanced()
    False
    >>> bst.isBalanced(2)
    False
    >>> bst.getAncestor(2, 9)
    7
    >>> bst.getAncestor(2, 9, 'bst')
    7
    >>> bst.getAncestor(2, 9, 'pre-post')
    7
    >>> bst.getAncestor(2, 9, 'post-in')
    7
    '''


    def addNode(self, value):
        ''' Add new node to the tree, by the left first, O(n).
            The only difference from the Binary Tree class is the node class is
            NodeBST and not NodeBT '''
        if not self.root: self.root = NodeBST(value)
        else: self.root._addNextNode(value) 
          


if __name__ == '__main__':
    import doctest
    doctest.testmod()

