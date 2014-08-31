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
'''


class NodeBT(object):
    def __init__(self, item=None, level=0):
        self.item = item
        self.level = level
        self.left = None
        self.right = None


    def __repr__(self):
        return '{}'.format(self.item)


    def _addNextNode(self, value, level_here=1):
        new_node = NodeBT(value, level_here)
        if not self.item:
            self.item = new_node
        elif not self.left:
            self.left = new_node
        elif not self.right:
            self.right = new_node
        else:
            self.left = self.left._addNextNode(value, level_here+1)
        return self ## this is important, because the node return to the main


    def _searchForNode(self, value):
        if self.item == value:
            return self
        else:
            found = None
            if self.left:
                found = self.left._searchForNode(value)
            if self.right:
                found =  found or self.right._searchForNode(value)
            return found


    def _isLeaf(self):
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
                 return  self.left._isBalanced()

    def _isBST(self, mintree=None, maxtree=None):
        ''' Find whether the tree is a BST, inorder '''
        if self.item:
            if not mintree:
                mintree = self.item
            if not maxtree:
                maxtree = self.item

            if self._isLeaf():
                return True
            elif self.left:
                if self.left.item < self.item and mintree > self.left.item:
                    mintree = self.left.item
                    return self.left._isBST(mintree, maxtree)
                else:
                    return False
            elif self.right:
                if self.right.item > self.item and maxtree < self.right.item:
                    maxtree = self.right.item
                    return self.right._isBST(mintree, maxtree)
                else:
                    return False
        else:
            print('Tree is empty')








class BinaryTree(object):

    def __init__(self):
        self.root = None


    def addNode(self, value):
        if not self.root:
            self.root = NodeBT(value)
        else:
            self.root._addNextNode(value)


    def isLeaf(self, value):
        node = self.root._searchForNode(value)
        if node:
            return node._isLeaf()
        else:
            print "Node not found."


    def getNodeLevel(self, item):
        node = self.root._searchForNode(item)
        if node:
            return node.level
        else:
            print('Node not found')


    def isRoot(self, value):
        return self.root.item == value


    def getHeight(self):
        return self.root._getMaxHeight()


    def isBalanced(self):
        return self.root._isBalanced()


    def isBST(self):
        return self.root._isBST()


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



if __name__ == '__main__':
    bt = BinaryTree()
    print "Adding nodes 1 to 10 in the tree..."
    for i in range(1, 10):
        bt.addNode(i)
    print "Is 8 a leaf? ", bt.isLeaf(8)
    print "Whats the level of node 8? ", bt.getNodeLevel(8)
    print "Is node 10 a root? ", bt.isRoot(10)
    print "Is node 1 a root? ", bt.isRoot(1)
    print "Whats the tree height? ", bt.getHeight()
    print "Is this tree BST? ", bt.isBST()
    print "Is this tree balanced? ", bt.isBalanced()
    print (bt.preorder())