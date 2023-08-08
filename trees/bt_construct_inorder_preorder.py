#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


def build_tree(preorder, inorder) -> Optional[Node]:
        
        def helper(left, right, index_map):
            
            if left > right:
                return None
            
            root = Node(preorder.pop(0))
            index_here = index_map[root.val]

            # this order change from postorder
            root.left = helper(left, index_here - 1, index_map)
            root.right = helper(index_here + 1, right, index_map)
            
            return root
        
        index_map = {value: i for i, value in enumerate(inorder)}
        
        return helper(0, len(inorder) - 1, index_map)
        
