#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

class Node:
    def __init__(self, val=0, next):
        self.val = val
        self.next = next


def reverse_list(head: Optional[Node]) -> Optional[Node]:

  if head is None:
            return head
        
    final_head = head
        
    while head.next:
      
        new_node = head.next
        head.next = new_node.next
        new_node.next = final_head
        final_head = new_node
        
    return final_head
        
