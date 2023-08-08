#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


def build_tree(left, right, index_map):
            
        if left > right:
                return None
            
        root = Node(postorder.pop())  # this order change from preorder
        index_here = index_map[root.val]

        root.right = build_tree(index_here + 1, right, index_map) # this order change from preorder
        root.left = build_tree(left, index_here - 1, index_map)
            
        return root


def build_tree(inorder, postorder) -> Optional[Node]:

        index_map = {val: i for i, value in enumerate(inorder)}
            
        return fill_tree(0, len(inorder) - 1, index_map)
    
