#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

def build_tree(preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        
        def helper(i_left, i_right, index_map):
            
            if i_left > i_right:
                return None
            
            root = TreeNode(preorder.pop(0))
            index_here = index_map[root.val]

            # this order change from postorder
            root.left = helper(i_left, index_here - 1, index_map)
            root.right = helper(index_here + 1, i_right, index_map)
            
            return root
            
        
        index_map = {value: index for index, value in enumerate(inorder)}
        
        return helper(0, len(inorder) - 1, index_map)
        
