#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
            
        if (not head) or (not head.next):
            return head
                
        new_head = reverse_list(head.next)
        head.next.next = head
        head.next = None
         
        return new_head
