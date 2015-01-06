#!/usr/bin/python

__author__ = "bt3"


from binary_tree import BinaryTree


def inorder(node, path=None):
    if node:
        path = path or []
        path.append(node.item)
        inorder(node.left, path)
        inorder(node.right, path)
    return path



def lowest_commom_ancestor(node, node1, node2):
    path = inorder(node.root)
    i1, i2 = 0, 0
    for i,n in enumerate(path):
        if n == node1:
            i1 = i
        if n == node2:
            i2 = i
    return path[i1:i2+1]






if __name__ == '__main__':
    bt = BinaryTree()
    l = [10, 6, 14, 3, 7, 11, 15]
    for i in l:
        bt.addNode(i)

    print(l)
    print(lowest_commom_ancestor(bt, 10, 6))
    print(lowest_commom_ancestor(bt, 10, 14))
    print(lowest_commom_ancestor(bt, 10, 3))
    print(lowest_commom_ancestor(bt, 10, 7))
    print(lowest_commom_ancestor(bt, 10, 11))
    print(lowest_commom_ancestor(bt, 10, 15))

