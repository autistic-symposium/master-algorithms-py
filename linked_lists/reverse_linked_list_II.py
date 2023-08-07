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

   prev = None
   curr = head
        
   while curr:
       next_temp = curr.next     // save the pointer for the next node so we can continue the loop
       curr.next = prev          // revert the list
       prev = curr               // save for the next node revert
       curr = next_temp          // receive the pointer for the next node so we can continue the loop

   return prev
       
