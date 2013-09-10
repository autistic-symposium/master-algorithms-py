#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

from BST import BST

class TranversalBST(object):
    def __init__(self):
        self.bst = BST(None)
        self.nodes = []
        
    def insert(self, value):
        if not self.bst.value:
            self.bst.value = value
        else:
            self.bst.insert(value)

    def contains(self, value):
        return bool(self.bst.find(value))

    def get(self, index):
        for i, value in enumerate(self.inorder()):
            if i == index:
                return value

    def inorder(self):
        current = self.bst  
        self.nodes = []
        stack = []
        while len(stack) > 0 or current is not None:
            if current is not None:
                stack.append(current)   
                current = current.left
            else:
                current = stack.pop()
                self.nodes.append(current.value)
                current = current.right
        return self.nodes


    def preorder(self):
        self.nodes = []
        stack = [self.bst]  
        while len(stack) > 0:
            curr = stack.pop()
            if curr is not None:
                self.nodes.append(curr.value)
                stack.append(curr.right)
                stack.append(curr.left)
        return self.nodes


    def preorder2(self):
        self.nodes = []
        current = self.bst  
        stack = []
        while len(stack) > 0 or current is not None:
            if current is not None:
                self.nodes.append(current.value)
                stack.append(current)   
                current = current.left
            else:
                current = stack.pop()               
                current = current.right            
        return self.nodes



def main():
    """
            10 
       5       15
    1   6     11    50
    """     
    t = TranversalBST()
    t.insert(10)
    t.insert(5)
    t.insert(15)
    t.insert(1)
    t.insert(6)
    t.insert(11)
    t.insert(50)
    print(t.preorder())
    print(t.preorder2())
    print(t.inorder())

if __name__ == '__main__':
    main()    
