#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

def postorder(root) -> list:
        
  if root is None:
      return []
    
  return postorder(root.left) + postorder(root.right) + [root.val] 
        
