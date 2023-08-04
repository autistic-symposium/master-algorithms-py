#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl



class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def dfs(prev, node):
  
        if not node:
            return prev

        node.prev = prev
        prev.next = node
        temp_next = node.next
  
        last = dfs(node, node.child)
        node.child = None
  
        return dfs(last, temp_next)


    def flatten(head):
        
        if head is None:
            return head

        pseudo_head = Node(None, None, head, None)
      
        dfs(pseudo_head, head)
        pseudo_head.next.prev = None
      
        return pseudo_head.next
