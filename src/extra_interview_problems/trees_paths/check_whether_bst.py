__author__ = "bt3"


""" need to keep track of min and max!!!"""

from binary_tree import BinaryTree, NodeBT
from binary_search_tree import BinarySearchTree, NodeBST

## my solution

def isBST(bt, mintree=None, maxtree=None):
    if not bt.item:
        return True

    if not mintree:
        mintree = bt.item

    if not maxtree:
        maxtree = bt.item

    left, right = False, False

    if bt.left:
        if bt.left.item > bt.item and bt.left.item < mintree:
            return False
        else:
            mintree = bt.left.item
            left = isBST(bt.left, mintree, maxtree)
    else:
        left = True
    if bt.right:
        if bt.right.item < bt.item and bt.right.item > maxtree:
            return False
        else:
            maxtree = bt.right.item
            right = isBST(bt.right, mintree, maxtree)
    else:
        right = True

    return  left and right









if __name__ == '__main__':
    bt = BinaryTree()
    print "Adding nodes 1 to 10 in the tree..."
    for i in range(1, 10):
        bt.addNode(i)

    print(isBST(bt.root))

    bst = BinarySearchTree()
    print "Adding nodes 1 to 10 in the tree..."
    for i in range(1, 10):
        bst.addNode(i)

    print(isBST(bst.root))
    print(bst.isBST())
