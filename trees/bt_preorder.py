#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

def preorder(root) -> list:
        
  if root is None:
      return []
    
  return [root.val] + preorder(root.left) + preorder(root.right)
        
