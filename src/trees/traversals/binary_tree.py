#!/usr/bin/python

__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"



''' Implementation of a binary tree and its properties. For example, the following bt:

                               1                ---> level 0
                        2             3         ---> level 1
                  4         5                   ---> level 2
              6      7                          ---> level 3
            8   9                               ---> level 4

    has the following properties:

        - SIZE OR NUMBER OF NODES: n = 9
        - NUMBER OF BRANCHES OR INTERNAL NODES: b = n-1 = 8
        - VALUE OF ROOT = 1
        - MAX_DEPTH OR HEIGHT: h = 4
        - IS BALANCED? NO
        - IS BST? NO
        - INORDER DFT: 8, 6, 9, 4, 7, 2, 5, 1, 3
        - POSTORDER DFT: 8, 9, 6, 7, 4, 5, 2, 3, 1
        - PREORDER DFT: 1, 2, 4, 6, 8, 9, 7, 5, 3
        - BFT:  1, 2, 3, 4, 5, 6, 7, 8, 9
'''

from collections import deque
class NodeBT(object):
    def __init__(self, item=None, level=0):
        ''' Construtor for a Node in the Tree '''
        self.item = item
        self.level = level
        self.left = None
        self.right = None
        self.traversal = []
        #self.parent = None # not used here but can be necessary for some problems

    '''
        METHODS TO MODIFY NODES
    '''

    def _addNextNode(self, value, level_here=1):
        ''' Aux for self.addNode(value)'''
        self.traversal = []
        new_node = NodeBT(value, level_here)
        if not self.item:
            self.item = new_node
        elif not self.left:
            self.left = new_node
        elif not self.right:
            self.right = new_node
        else:
            self.left = self.left._addNextNode(value, level_here+1)
        return self



    '''
        METHODS TO PRINT/SHOW NODES' ATTRIBUTES
    '''

    def __repr__(self):
        ''' Private method for this class'string representation'''
        return '{}'.format(self.item)

    def _getDFTpreOrder(self, node):
        ''' Traversal Pre-Order, O(n)'''
        if node:
            if node.item: self.traversal.append(node.item)
            self._getDFTpreOrder(node.left)
            self._getDFTpreOrder(node.right)
        return self

    def _printDFTpreOrder(self, noderoot):
        ''' Fill the pre-order traversal array '''
        self.traversal = []
        self._getDFTpreOrder(noderoot)
        return self.traversal

    def _getDFTinOrder(self, node):
        ''' Traversal in-Order, O(n)'''
        if node:
            self._getDFTinOrder(node.left)
            if node.item: self.traversal.append(node.item)
            self._getDFTinOrder(node.right)
        return self

    def _printDFTinOrder(self, noderoot):
        ''' Fill the in-order traversal array '''
        self.traversal = []
        self._getDFTinOrder(noderoot)
        return self.traversal

    def _getDFTpostOrder(self, node):
        ''' Traversal post-Order, O(n)'''
        if node:
            self._getDFTpostOrder(node.left)
            self._getDFTpostOrder(node.right)
            if node.item: self.traversal.append(node.item)
        return self

    def _getBFT(self, node):
        ''' Traversal bft, O(n)'''
        if node:
            queue = deque()
            queue.append(node)
            while len(queue) > 0:
                current = queue.popleft()
                if current.item: self.traversal.append(current)
                if current.left: queue.append(current.left)
                if current.right: queue.append(current.right)
        return self

    def _printBFT(self, noderoot):
        ''' Fill the in-order traversal array '''
        self.traversal = []
        self._getBFT(noderoot)
        return self.traversal


    def _printDFTpostOrder(self, noderoot):
        ''' Fill the post-order traversal array '''
        self.traversal = []
        self._getDFTpostOrder(noderoot)
        return self.traversal

    def _searchForNode(self, value):
        ''' Traverse the tree looking for the node'''
        if self.item == value: return self
        else:
            found = None
            if self.left: found = self.left._searchForNode(value)
            if self.right: found =  found or self.right._searchForNode(value)
            return found

    def _findNode(self, value):
        ''' Find whether a node is in the tree.
            if the traversal was calculated, it is just a membership
            checking, which is O(1), otherwise it is necessary to traverse
            the binary tree, so best case is O(1) and worst is O(n). '''
        if self.traversal: return value in self.traversal
        else: return self._searchForNode(value)

    def _isLeaf(self):
        ''' Return True if the node is a leaf '''
        return not self.right and not self.left

    def _getMaxHeight(self):
        ''' Get the max height at the node, O(n)'''
        levelr, levell = 0, 0
        if self.right:
            levelr = self.right._getMaxHeight() + 1
        if self.left:
            levell = self.left._getMaxHeight() + 1
        return max(levelr, levell)

    def _getMinHeight(self, level=0):
        ''' Get the min height at the node, O(n)'''
        levelr, levell = -1, -1
        if self.right:
            levelr = self.right._getMinHeight(level +1)
        if self.left:
            levell = self.left._getMinHeight(level +1)
        return min(levelr, levell) + 1

    def _isBalanced(self):
        ''' Find whether the tree is balanced, by calculating heights first, O(n2) '''
        if self._getMaxHeight() - self._getMinHeight() < 2:
            return False
        else:
            if self._isLeaf():
                return True
            elif self.left and self.right:
                return self.left._isBalanced() and   self.right._isBalanced()
            elif not self.left and self.right:
                return  self.right._isBalanced()
            elif not self.right and self.left:
                 return  self.right._isBalanced()



    def _isBalancedImproved(self):
        ''' Find whehter the tree is balanced in each node, O(n) '''
        return 'To Be written'

    ''' There are two solutions to check whether a bt is a bst:
    (1) Do an inorder, check if the inorder is sorted. However inorder
        can't handle the difference between duplicate values on the left
        or on the right (if it is in the right, the tree is not bst).
    '''


    def _isBST(self):
        ''' Find whether the tree is a BST, inorder '''
        if self.item:
            if self._isLeaf(): return True
            elif self.left:
                if self.left.item < self.item: return self.left._isBST()
                else: return False
            elif self.right:
                if self.right.item > self.item: return self.right._isBST()
                else: return False
        else:
            raise Exception('Tree is empty')


    def _getAncestorBST(self, n1, n2):
        ''' Return the ancestor of two nodes if it is a bst.
            we are supposing the values in the tree are unique.'''
        if n1 == self.item or n2 == self.item : return self.item
        elif self.item < n1 and self.item < n2:
            self.right.getAncestorBST(n1, n2)
        elif self.item > n1 and self.item > n2:
            self.left.getAncestorBST(n1, n2)
        else:
            return self.item




class BinaryTree(object):
    '''
    >>> bt = BinaryTree()
    >>> for i in range(1, 10): bt.addNode(i)
    >>> bt.hasNode(7)
    True
    >>> bt.hasNode(12)
    False
    >>> bt.printTree()
    [1, 2, 4, 6, 8, 9, 7, 5, 3]
    >>> bt.printTree('pre')
    [1, 2, 4, 6, 8, 9, 7, 5, 3]
    >>> bt.printTree('bft')
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> bt.printTree('post')
    [8, 9, 6, 7, 4, 5, 2, 3, 1]
    >>> bt.printTree('in')
    [8, 6, 9, 4, 7, 2, 5, 1, 3]
    >>> bt.hasNode(9)
    True
    >>> bt.hasNode(11)
    False
    >>> bt.isLeaf(8)
    True
    >>> bt.getNodeLevel(1)
    0
    >>> bt.getNodeLevel(8)
    4
    >>> bt.getSizeTree()
    9
    >>> bt.isRoot(10)
    False
    >>> bt.isRoot(1)
    True
    >>> bt.getHeight()
    4
    >>> bt.isBST(1)
    False
    >>> bt.isBalanced()
    False
    >>> bt.isBalanced(2)
    False
    >>> bt.getAncestor(8, 5)
    2
    >>> bt.getAncestor(8, 5, 'pre-post')
    2
    >>> bt.getAncestor(8, 5, 'post-in')
    2
    '''



    def __init__(self):
        ''' Constructor for the Binary Tree, which is a container of Nodes'''
        self.root = None


    '''
        METHODS TO MODIFY THE TREE
    '''

    def addNode(self, value):
        ''' Add new node to the tree, by the left first, O(n) '''
        if not self.root: self.root = NodeBT(value)
        else: self.root._addNextNode(value)

    '''
        METHODS TO PRINT/SHOW TREES' ATTRIBUTES
    '''

    def __repr__(self):
        ''' Private method for this class'string representation'''
        return '{}'.format(self.item)

    def printTree(self, order = 'pre'):
        ''' Print Tree in the chosen order '''
        if self.root:
            if order == 'pre': return self.root._printDFTpreOrder(self.root)
            elif order == 'in': return self.root._printDFTinOrder(self.root)
            elif order == 'post': return self.root._printDFTpostOrder(self.root)
            elif order == 'bft': return self.root._printBFT(self.root)
        else: raise Exception('Tree is empty')

    def hasNode(self, value):
        ''' Verify whether the node is in the Tree '''
        return bool(self.root._findNode(value))

    def isLeaf(self, value):
        ''' Return True if the node is a Leaf '''
        node = self.root._searchForNode(value)
        return node._isLeaf()

    def getNodeLevel(self, item):
        ''' Return the level of the node, best O(1), worst O(n) '''
        node = self.root._searchForNode(item)
        if node: return node.level
        else: raise Exception('Node not found')

    def getSizeTree(self):
        ''' Return how many nodes in the tree, O(n) '''
        return len(self.root._printDFTpreOrder(self.root))

    def isRoot(self, value):
        '''Return the root of the tree '''
        return self.root.item == value

    def getHeight(self):
        ''' Returns the height/depth of the tree, best/worst O(n)  '''
        return self.root._getMaxHeight()

    def isBalanced(self, method=1):
        ''' Return True if the tree is balanced'''
        if method == 1:
            ''' O(n2)'''
            return self.root._isBalanced()
        else:
            ''' O(n)'''
            return self.root._isBalancedImproved()



    ''' The following methods are for searching the lowest common ancestor
    in a BT. Since a simple BT does not have ordering, it can be O(n). If
    we have a link for the ancestors, the steps are:
        (1) search both trees in order to find the nodes separately
        (2) list all ancestors
        (3) find first that mach
        obs: if we do this too many times we can do a pre and use the methods here'''

    def isBST(self, method=1):
        ''' Return True if the tree is BST'''
        if method == 1:
            inorder = self.root._printDFTinOrder(self.root)
            return inorder == sorted(inorder)
        elif method == 2:
            return self.root._isBST()


    def _getAncestorPreIn(self, preorder, inorder, value1, value2):
        ''' Return the ancestor of two nodes with pre and in'''
        root = preorder[0]
        preorder = preorder[1:]
        i = 0
        item = inorder[0]
        value1left, value2left = False, False
        while item != root and i < len(inorder):
            if item == value1: value1left = True
            elif item == value2: value2left = True
            i += 1
            item = inorder[i]
        if (value1left and not value2left) or (value2left and not value1left):
            return root
        else:
            return self._getAncestorPreIn(preorder, inorder[:i] + inorder[i+1:], value1, value2)

    def _getAncestorPrePost(self, preorder, postorder, value1, value2):
        ''' Return the ancestor of two nodes with pre and post'''
        root = preorder[0]
        preorder = preorder[1:]
        postorder = postorder[:-1]
        value1right, value2right = False, False
        i = len(postorder)-1
        itempre = preorder[0]
        itempos = postorder[i]
        while itempre != itempos and i > 0:
            if itempos == value1: value1right = True
            elif itempos == value2: value2right = True
            i -= 1
            itempos = postorder[i]

        if (value1right and not value2right) or (value2right and not value1right):
            return root
        else:
            return self._getAncestorPrePost(preorder, postorder[:i] + postorder[i+1:], value1, value2)

    def _getAncestorInPost(self, inorder, postorder, value1, value2):
        ''' Return the ancestor of two nodes with in and post'''
        root = postorder[-1]
        postorder = postorder[:-1]
        value1left, value2left = False, False
        i = 0
        item = inorder[i]
        while item != root and i < len(inorder):
            if item == value1: value1left = True
            elif item == value2: value2left = True
            i += 1
            item = inorder[i]

        if (value1left and not value2left) or (value2left and not value1left):
            return root
        else:
            return self._getAncestorInPost(postorder, inorder[:i] + inorder[i+1:], value1, value2)





    def _getAncestorBST2(self, preorder, value1, value2):
        ''' Return the ancestor of two nodes if it is a bst, using traversal'''
        while preorder:
            current = preorder[0]
            if current < value1:
                try: preorder = preorder[2:]
                except: return current
            elif current > value2:
                try: preorder = preorder[1:]
                except: return current
            elif value1 <= current <= value2:
                return current
        return None

    def getAncestor(self, value1, value2, method='pre-in'):
        ''' Return the commom ancestor for two nodes'''
        if method == 'pre-in':
            ''' Using pre and inorder, best/worst O(n)'''
            preorder = self.root._printDFTpreOrder(self.root)
            inorder = self.root._printDFTinOrder(self.root)
            return self._getAncestorPreIn(preorder, inorder, value1, value2)
        if method == 'pre-post':
            ''' Using pre and postorder, best/worst O(n)'''
            preorder = self.root._printDFTpreOrder(self.root)
            postorder = self.root._printDFTpostOrder(self.root)
            return self._getAncestorPrePost(preorder, postorder, value1, value2)
        if method == 'post-in':
            ''' Using in and postorder, best/worst O(n)'''
            inorder = self.root._printDFTinOrder(self.root)
            postorder = self.root._printDFTpostOrder(self.root)
            return self._getAncestorInPost(inorder, postorder, value1, value2)
        if method == 'bst':
            if self.isBST():
                return self.root._getAncestorBST(value1, value2)

                #preorder = self.root._printDFTpreOrder(self.root)
                #return self._getAncestorBST2(preorder, value1, value2)
            else:
                return Exception('The tree is not a BST')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
