#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl
# this is my favorite implementation <3


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class CircularQueue:

    def __init__(self, k: int):
      
        self.capacity = k
        self.count = 0
        self.head = None
        self.tail = None
        
    def enqueue(self, value: int) -> bool:

        if self.count == self.capacity:
            return False
        
        if self.count == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
          
        self.count += 1
      
        return True

    def dequeue(self) -> bool:

        if self.count == 0:
            return False
          
        self.head = self.head.next
        self.count -= 1
      
        return True

    def front(self) -> int:

        if self.count == 0:
            return -1
          
        return self.head.value

    def rear(self) -> int:

        if self.count == 0:
            return -1
          
        return self.tail.value
    
    def is_empty(self) -> bool:

        return self.count == 0

    def is_full(self) -> bool:

        return self.count == self.capacity
      
