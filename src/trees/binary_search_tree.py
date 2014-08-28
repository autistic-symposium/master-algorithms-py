#!/usr/bin/python

__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"


from binary_tree import NodeBT, BinaryTree


class NodeBST(NodeBT):

    def __init__(self, item=None, level=0):
        self.item = item
        self.level = level
        self.left = None
        self.right = None


    def _addNextNode(self, value, level_here=1):
        new_node = NodeBST(value, level_here)
        if not self.item:
            self.item = new_node
        else:
            if value > self.item:
                self.right = self.right and self.right._addNextNode(value, level_here+1) or new_node
            elif value < self.item:
                self.left = self.left and self.left._addNextNode(value, level_here+1) or new_node
            else:
                print("BSTs do not support repeated items.")
        return self # this is necessary!!!



    def _searchForNode(self, value):
        if self.item == value:
            return self
        elif self.left and value < self.item:
                return self.left._searchForNode(value)
        elif self.right and value > self.item:
                return self.right._searchForNode(value)
        else:
            return False



class BinarySearchTree(BinaryTree):

    def __init__(self):
        self.root = None

    def addNode(self, value):
        if not self.root:
            self.root = NodeBST(value)
        else:
            self.root._addNextNode(value)




if __name__ == '__main__':
    bst = BinarySearchTree()
    print "Adding nodes 1 to 10 in the tree..."
    for i in range(1, 10):
        bst.addNode(i)
    print "Is 8 a leaf? ", bst.isLeaf(8)
    print "Whats the level of node 8? ", bst.getNodeLevel(8)
    print "Is node 10 a root? ", bst.isRoot(10)
    print "Is node 1 a root? ", bst.isRoot(1)
    print "Whats the tree height? ", bst.getHeight()
    print "Is this tree BST? ", bst.isBST()
    print "Is this tree balanced? ", bst.isBalanced()


