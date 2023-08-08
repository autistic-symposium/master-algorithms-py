#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


def bfs_iterative(root) -> list:

        result = []
        queue = collections.deque([root])
        
        while queue:
    
            node = queue.popleft()
                
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        
        return result


def bfs_recursive(root) -> list:

        result = []

        def helper(node):
        
            if node:
                result.append(node.val)
                helper(node.left)
                helper(node.right)
        
        helper(root)
        return result
        
