#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

def search_bst(root, val):
        
        if root is None or root.val == val:
            return root
        
        if val > root.val:
            return search_bst(root.right, val)
        
        else:
            return search_bst(root.left, val) 
        
