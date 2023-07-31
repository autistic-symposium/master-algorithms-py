#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next


def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
      if not head or not head.next:
          return head

      ## nodes to be swapped
      first_node = head
      second_node = head.next

      # swapping
      first_node.next = swap_pairs(second_node.next)
      second_node.next = first_node

      return second_node
