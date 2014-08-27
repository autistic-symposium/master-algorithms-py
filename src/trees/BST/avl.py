#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

from BST_with_Nodes import BSTwithNodes, Node


class AVL(BSTwithNodes):
    """AVL binary search tree implementation.
    Supports insert, find, and delete-min operations in O(lg n) time.
    """
    def __init__(self): 
        self.root = None

    def left_rotate(self, x):
        y = x.right
        y.value = x.value
        if y.value is None:
            self.root = y
        else:
            if y.value.left is x:
                y.value.left = y
            elif y.value.right is x:
                y.value.right = y
        x.right = y.left
        if x.right is not None:
            x.right.value = x
        y.left = x
        x.value = y
        update_height(x)
        update_height(y)

    def right_rotate(self, x):
        y = x.left
        y.value = x.value
        if y.value is None:
            self.root = y
        else:
            if y.value.left is x:
                y.value.left = y
            elif y.value.right is x:
                y.value.right = y
        x.left = y.right
        if x.left is not None:
            x.left.value = x
        y.right = x
        x.value = y
        update_height(x)
        update_height(y)

    def insert_item(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(value)
                        break;      

                elif value > current.value:               
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(value)
                        break;      
                else:
                    break 


    def insert(self, value):
        node = self.insert_item(value)
        self.rebalance(node)
        
        
    def rebalance(self, node):
        while node is not None:
            update_height(node)
            if height(node.left) >= 2 + height(node.right):
                if height(node.left.left) >= height(node.left.right):
                    self.right_rotate(node)
                else:
                    self.left_rotate(node.left)
                    self.right_rotate(node)
            elif height(node.right) >= 2 + height(node.left):
                if height(node.right.right) >= height(node.right.left):
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.right)
                    self.left_rotate(node)
            node = node.value


    def inorder(self, node):       
        if node is not None:         
            self.inorder(node.left)
            print(node.value)
            self.inorder(node.right)

    def preorder(self, node):           
        if node is not None:    
            print(node.value)
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):           
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value)


def height(node):
    if node is None: return -1
    else: return node.height

def update_height(node):
    node.height = max(height(node.left), height(node.right)) + 1



def main():
    tree = AVL()
    tree.insert(4)
    tree.insert(2)
    tree.insert(6)
    tree.insert(1)
    tree.insert(3)
    tree.insert(7)
    tree.insert(5)
    print('Inorder Traversal:')
    tree.inorder(tree.root) 



if __name__ == '__main__':
    main()
