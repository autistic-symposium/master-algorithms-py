#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

def remove_elements(head, val):
        
  sentinel = ListNode(0)
  sentinel.next = head
  prev, current = sentinel, head

  while current:
    if current.val == val:
      prev.next = current.next
    else:
      prev = current
    current = current.next
                
  return sentinel.next
  
