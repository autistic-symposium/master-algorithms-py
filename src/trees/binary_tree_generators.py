#!/usr/bin/env python

__author__ = "bt3"


class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def add(self, value):
        new_node = Node(value)
        if not self.value:
            self.value = new_node
        elif not self.left:
            self.left= new_node
        elif not self. right:
            self.right = new_node
        else:
            self.left = self.left.add(value)

        return self # without this, it doesn't add!

    def preorder(self):
        yield self.value
        if self.left:
            for node in self.left.preorder():
                yield node
        if self.right:
            for node in self.right.preorder():
                yield node

    def postorder(self):
        yield self.value
        if self.left:
            for node in self.left.postorder():
                yield node
        if self.right:
            for node in self.right.postorder():
                yield node


    def inorder(self):
        yield self.value
        if self.left:
            for node in self.left.inorder():
                yield node
        if self.right:
            for node in self.right.inorder():
                yield node


    # Another possibility: use an array (a little bit more expensive):
    def preorder_array(self):
        nodes = []
        if self.value:
            nodes.append(self.value)
        if self.left:
            nodes.extend(self.left.preorder_array())
        if self.right:
            nodes.extend(self.right.preorder_array())
        return nodes



class BT(object):
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self.root.add(value)

    def preorder(self):
        if self.root:
            return self.root.preorder()
        else:
            return 'Tree is empty.'

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return 'Tree is empty.'

    def postorder(self):
        if self.root:
            return self.root.postorder()
        else:
            return 'Tree is empty.'

    def preorder_array(self):
        if self.root:
            return self.root.preorder_array()
        else:
            return 'Tree is empty.'



if __name__ == '__main__':
    tree = BT()

    for i in range(1, 11):
        tree.add(i)

    getree = tree.preorder()
    for i in range(10):
        print next(getree)

    print

    print tree.preorder_array()

    print

    getree = tree.inorder()
    for i in range(10):
        print next(getree)

    print

    getree = tree.postorder()
    for i in range(10):
        print next(getree)
