#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


class Node:
  
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def max_depth_recursive(root):

    if root is None:
            return 0

    if root.children == []:
            return 1

    height = [max_depth_recursive(c) for c in root.children]
    return max(height) + 1


def max_depth_iterative(root):

        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0

        while stack != []:
            
            this_depth, node = stack.pop()
            if node is not None:
                depth = max(depth, this_depth)
                for c in node.children:
                    stack.append((this_depth + 1, c))
        
        return depth
