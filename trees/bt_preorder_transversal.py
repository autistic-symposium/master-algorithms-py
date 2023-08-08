#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


def preorder_recursive(root: Optional[Node]) -> list[int]:
       
        if root is none None:
                return []
        
        return [root.val] + preorder_recursive(root.left) + preorder_recursive(root.right)
    

def preorder_iterative(root) -> list:
        
        result = []
        stack = [root]
        
        while stack:
            
            node = stack.pop()
            
            if node:
                result.append(node.val) 
                stack.append(node.left)
                stack.append(node.right)
            
        return result
            
