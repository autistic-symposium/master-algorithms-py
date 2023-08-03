#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


class Tree:
    
    def lowest_common_ancestor(self, root, p, q):
        
        def dfs(root, p, q):

            if not root:
                return False
            
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)
            mid = root == p or root == q

            if mid + left + right >= 2:
                self.answer = root
            
            return left or right or mid
                
        dfs(root, p, q)
        
        return self.answer
    
