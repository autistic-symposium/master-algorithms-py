#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


def bst_insert_iterative(root, val):

  new_node = Node(val)
  this_node = root
  
  while this_node:
    
    if  val > this_node.val:
        if not this_node.right:
          this_node.right = new_node
          return root
        else:
          this_node = this_node.right
    
    else:
        if not this_node.left:
          this_node.left = new_node
          return this_node
        else:
          this_node = this_node.left
        
  return new_node


def bst_insert_recursive(root, val):
        
    if not root:
        return Node(val)

    if val > root.val:
        root.right = self.insertIntoBST(root.right, val)
        
    else:
        root.left = self.insertIntoBST(root.left, val)
        
    return root
            
