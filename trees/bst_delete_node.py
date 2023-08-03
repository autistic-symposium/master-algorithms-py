#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


def successor(root):
   
    root = root.right
    while root.left:
            root = root.left
    return root.val


def predecessor(root):
  
    root = root.left
    while root.right:
            root = root.right
    return root.val


def delete_node(root, key):
        
    if not root:
            return root

    if key > root.val:
            root.right = deleteNode(root.right, key)
      
    elif key < root.val:
            root.left = deleteNode(root.left, key)
      
    else:
        if not (root.left or root.right):
            root = None
          
        elif root.right:
            root.val = successor(root)
            root.right = deleteNode(root.right, root.val)
          
        else:
            root.val = predecessor(root)
            root.left = deleteNode(root.left, root.val)
        
    return root
        
