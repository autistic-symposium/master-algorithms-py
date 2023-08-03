#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

def search_bst_recursive(root, val):
        
        if root is None or root.val == val:
            return root
        
        if val > root.val:
            return search_bst_recursive(root.right, val)
        
        else:
            return search_bst_recursive(root.left, val) 


        
def search_bst_iterative(root, val):
        
        node = root
        while node:
            
            if node.val == val:
                return node

            if node.val < val:
                node = node.right

            else:
                node = node.left
        
        return False
