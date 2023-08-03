#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


def remove_kth_node(self, head, n):
  
        if head is None or head.next is None:
            return None
        
        node = head
        lenght = 0
        
        # find the lenght of the list
        while node:
            node = node.next
            lenght += 1
            
        if n == lenght:
            return head.next
    
        i = 0
        node = head
        while i < lenght - n - 1:
            node = node.next
            i += 1
        
        node.next = node.next.next
                
        return head
        
