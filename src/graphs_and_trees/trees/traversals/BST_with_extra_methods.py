#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

from BST_traversal import TranversalBST
from BST import BST

class BSTwithExtra(TranversalBST):
    def __init__(self):
        self.bst = BST(None)
        self.nodes = []  
                      
    def get_inorder(self, k):
        for i, value in enumerate(self.inorder()):
            if value == k:
                return i
                
    def get_preorder(self, k):
        for i, value in enumerate(self.preorder()):
            if value == k:
                return i
                                    

    def is_balanced(self, threshold=1):
        maxd = self.get_max_depth()
        mind = self.get_min_depth()
        print('Max depth: ' + str(maxd))
        print('Min depth: ' + str(mind))
        return maxd -mind

    def get_min_depth(self, node=None, initial=1):
        if node is None and initial == 1:
            node = self.bst
        if node.left and node.right:
            return 1 + min(self.get_min_depth(node.left, 0),
                       self.get_min_depth(node.right, 0))
        else:
            if node.left:
                return 1 + self.get_max_depth(node.left, 0)
            elif node.right:
                return 1 + self.get_max_depth(node.right, 0)
            else:
                return 0
    
    def get_max_depth(self, node=None, initial=1):
        if node is None and initial == 1:
            node = self.bst
        if node.left and node.right:
            return 1 + max(self.get_max_depth(node.left, 0),
                       self.get_max_depth(node.right, 0))
        else:
            if node.left:
                return 1 + self.get_max_depth(node.left, 0)
            elif node.right:
                return 1 + self.get_max_depth(node.right, 0)
            else:
                return 0

def main():
    """
            10 
       5       15
    1   6     11    50
                        60
                            70
                                80
    """     
    t = BSTwithExtra()
    l1 = [10, 5, 15, 1, 6, 11, 50, 60, 70, 80]
    for i in l1: t.insert(i)
    print(t.inorder())
    print(t.preorder())
    assert(t.get_max_depth() == 5)
    assert(t.get_min_depth() == 2)
    assert(t.is_balanced() == 3)    
    assert(t.get_inorder(10) == 3)
    assert(t.get_preorder(10) == 0)    
    
    
    """
            1 
       2       3
    4   5     6    7
    """  
    t2 = BSTwithExtra()
    l2 = [1, 2, 3, 4, 5, 6, 7, 8]
    for i in l2: t2.insert(i)
    print(t2.inorder())
    print(t2.preorder())
    assert(t2.is_balanced() == 0)    
   
    print("Tests Passed!")

if __name__ == '__main__':
    main()
