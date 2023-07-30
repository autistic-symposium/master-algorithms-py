#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

'''
Given the root of a binary tree, return the number of uni-value subtrees.
A uni-value subtree means all nodes of the subtree have the same value.
'''
 
def count_unival(root: Optional[TreeNode]) -> int:
        
        global count = 0
        
        def dfs(node):
            
            if not node:
                return True
        
            is_uni_left = dfs(node.left)
            is_uni_right = dfs(node.right)
            
            if is_uni_left and is_uni_right:
                if node.left and node.left.val != node.val:
                    return False
                if node.right and node.right.val != node.val:
                    return False
            
                self.count += 1
                return True
            
            return False

        dfs(root)
        return count
