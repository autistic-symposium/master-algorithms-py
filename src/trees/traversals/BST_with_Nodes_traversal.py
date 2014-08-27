#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

from BST_with_Nodes import BSTwithNodes, Node

class BSTTraversal(BSTwithNodes):
    def __init__(self): 
        self.root = None
        self.nodes_BFS = []
        self.nodes_DFS_pre = []
        self.nodes_DFS_post = []
        self.nodes_DFS_in = []

    def BFS(self): 
        self.root.level = 0 
        queue = [self.root]
        current_level = self.root.level

        while len(queue) > 0:                 
            current_node = queue.pop(0)
            if current_node.level > current_level:
                current_level += 1
            self.nodes_BFS.append(current_node.value)

            if current_node.left:
                current_node.left.level = current_level + 1
                queue.append(current_node.left)
                  
            if current_node.right:
                current_node.right.level = current_level + 1
                queue.append(current_node.right)
      
        return self.nodes_BFS 

    def DFS_inorder(self, node):      
        if node is not None:         
            self.DFS_inorder(node.left)
            self.nodes_DFS_in.append(node.value)
            self.DFS_inorder(node.right)
        return self.nodes_DFS_in

    def DFS_preorder(self, node):          
        if node is not None:    
            self.nodes_DFS_pre.append(node.value)
            self.DFS_preorder(node.left)
            self.DFS_preorder(node.right)
        return self.nodes_DFS_pre

    def DFS_postorder(self, node):           
        if node is not None:
            self.DFS_postorder(node.left)
            self.DFS_postorder(node.right)
            self.nodes_DFS_post.append(node.value)
        return self.nodes_DFS_post

def main():
    tree = BSTTraversal()     
    l1 = [10, 5, 15, 1, 6, 11, 50]
    for i in l1: tree.insert(i)
    
    print('Breadth-First Traversal: ', tree.BFS())    
    print('Inorder Traversal: ', tree.DFS_inorder(tree.root))   
    print('Preorder Traversal: ', tree.DFS_preorder(tree.root))
    print('Postorder Traversal: ', tree.DFS_postorder(tree.root)) 

if __name__ == '__main__':
    main()
