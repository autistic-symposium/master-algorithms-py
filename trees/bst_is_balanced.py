#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


def height(root):
  
    if not root:
      return -1
      
    return 1 + max(height(root.left), height(root.right))


def is_balanced(root):
  
    if not root:
      return True

    return abs(height(root.left) - height(root.right)) < 2 and \
            is_balanced(root.left) and is_balanced(root.right)
        
