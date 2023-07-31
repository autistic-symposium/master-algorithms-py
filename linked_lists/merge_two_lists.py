#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next


def merge_two_list(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        if list1.val < list2.val:
            list1.next = merge_two_list(list1.next, list2)
            return list1
        else:
            list2.next = merge_two_list(list1, list2.next)
            return list2
            
