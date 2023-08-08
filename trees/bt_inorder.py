#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

def inorder(root) -> list:
        
  if root is None:
      return []
    
  return inorder(root.left) + [root.val] + inorder(root.right)
        
