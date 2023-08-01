#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

class CircularQueue:

    def __init__(self, k: int):
        self.head = -1
        self.tail = -1
        self.size = k
        self.queue = [None] * self.size
        
    def _get_next_position(self, end) -> int:
        return (end + 1) % self.size
        
    def enqueue(self, value: int) -> bool:

        if self.is_full():
            return False

        if self.is_empty() :
            self.head = 0;
        
        self.tail = self._get_next_position(self.tail)
        self.queue[self.tail] = value

        return True

    def dequeue(self) -> bool:

        if self.is_empty():
            return False

        if self.head == self.tail:
            self.head = -1
            self.tail = -1
            return True
        
        self.head = self._get_next_position(self.head)

        return True

    def Front(self) -> int:
        if self.is_empty():
            return -1
        return self.queue[self.head]
        
    def Rear(self) -> int:
        if self.is_empty():
            return -1
        return self.queue[self.tail]
        
    def is_empty(self) -> bool:
        return self.head == -1

    def is_full(self) -> bool:
        return self._get_next_position(self.tail) == self.head
        
