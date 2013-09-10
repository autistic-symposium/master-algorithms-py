#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

from BT import BT

class BST(BT):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, new_node):
        self.insert(value)
        
    def insert_right(self, new_node):
        self.insert(value)


    def insert(self, value):
        if  self.value == None:
            self.value = value
        else:
            if value > self.value:
                self.right = self.right and self.right.insert(value) or BST(value)
            else:
                self.left = self.left and self.left.insert(value) or BST(value)
        return self

    def find(self, value):
        if value == self.value:
            return self
        elif value > self.value and self.right:
            return self.right.find(value)
        elif self.left:
            return self.left.find(value)
        return None




def main():
    """
    BST
          4
       2     6
     1   3 5   7
    """
    tree = BST()
    tree.insert(4)
    tree.insert(2)
    tree.insert(6)
    tree.insert(1)
    tree.insert(3)
    tree.insert(7)
    tree.insert(5)
    print(tree.get_right())
    print(tree.get_right().get_left())
    print(tree.get_right().get_right())
    print(tree.get_left())
    print(tree.get_left().get_left())
    print(tree.get_left().get_right() == 1)
    assert(tree.find(30) == None)


if __name__ == '__main__':
    main()

