#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


def rotate_list_by_k(head, k):
        
    if head is None and head.next is None:
        return None
        
    end, new_end, n = head, head, 1
        
    while end.next:
        end = end.next
        n += 1
    end.next = head

    for i in range(n - k % n - 1):
        new_end = new_end.next
            
    new_head = new_end.next
    new_end.next = None
        
    return new_head
  
