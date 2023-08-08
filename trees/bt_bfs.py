#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


def bfs_iterative(root) -> list:

        result = []
        queue = collections.deque([root])
        
        if root is None:
            return result
        
        while queue:
    
            node = queue.popleft()
                
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        
        return result


def bfs_recursive(root) -> list:

        result = []
        if root is None:
            return root
        
        def helper(node):
        
            if node:
                result.append(node.val)
                helper(node.left)
                helper(node.right)
        
        helper(root)
        return result
        
