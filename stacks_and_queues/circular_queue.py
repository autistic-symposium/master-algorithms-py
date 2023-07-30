#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

## implement a circular queue


class CircularQueue:

    def __init__(self, k: int):
        self.head = 0
        self.tail = 0
        self.size = k
        self.queue = [None] * self.size
        
    def enQueue(self, value: int) -> bool:

        if value is None:
            return False
            
        if self.isFull():
            return False

        if self.isEmpty():
            self.heard = 0
        
        while self.queue[self.tail] != None:
            self.tail += 1 
            if self.tail == self.size:
                self.tail = 0
    
        self.queue[self.tail] = value
        return True

    def deQueue(self) -> bool:

        if self.isEmpty():
            return False

        value = self.queue[self.head]
        self.queue[self.head] = None
        self.head += 1

        if self.head == self.size:
            self.head = 0

        return True

    def Front(self) -> int:
        return self.queue[self.head] or -1
        
    def Rear(self) -> int:
        return self.queue[self.tail] or -1
        
    def isEmpty(self) -> bool:
        for n in self.queue:
            if n is not None:
                return False
        return True

    def isFull(self) -> bool:
        for n in self.queue:
            if n is None:
                return False
        return True
        

if __name__ == "__main__":

    q = CircularQueue(5)
    print(f'q: {q.queue}')
    print(f'q.isEmpty(): {q.isEmpty()}')
    print(f'q.isFull(): {q.isFull()}')
    print(f'q.enQueue(1): {q.enQueue(1)}')
    print(f'h: {q.head}, t: {q.tail}')
    print(f'q.enQueue(2): {q.enQueue(2)}')
    print(f'h: {q.head}, t: {q.tail}')
    print(f'q.enQueue(3): {q.enQueue(3)}')
    print(f'h: {q.head}, t: {q.tail}')
    print(f'q.enQueue(4): {q.enQueue(4)}')
    print(f'h: {q.head}, t: {q.tail}')
    print(f'isFull(): {q.isFull()}')
    print(f'q.enQueue(5): {q.enQueue(5)}')
    print(f'h: {q.head}, t: {q.tail}')
    print(f'isFull(): {q.isFull()}')
    print(f'q.isEmpty(): {q.isEmpty()}')
    print(f'q: {q.queue}')
    print(f'q.enQueue(6): {q.enQueue(6)}')
    print(f'h: {q.head}, t: {q.tail}')
    print(f'isFull(): {q.isFull()}')
    print(f'q.isEmpty(): {q.isEmpty()}')
    print()
    print(f'q.deQueue(): {q.deQueue()}')
    print(f'q: {q.queue}')
    print(f'h: {q.head}, t: {q.tail}')
    print(f'q.deQueue(): {q.deQueue()}')
    print(f'q: {q.queue}')
    print(f'h: {q.head}, t: {q.tail}')
    print(f'q.deQueue(): {q.deQueue()}')
    print(f'q: {q.queue}')
    print(f'h: {q.head}, t: {q.tail}')
    print(f'q.deQueue(): {q.deQueue()}')
    print(f'q: {q.queue}')
    print(f'h: {q.head}, t: {q.tail}')
    print(f'q.deQueue(): {q.deQueue()}')
    print(f'q: {q.queue}')
    print(f'h: {q.head}, t: {q.tail}')
    print(f'q.deQueue(): {q.deQueue()}')
    print(f'q: {q.queue}')
    print(f'h: {q.head}, t: {q.tail}')
    print(f'q.Front(): {q.Front()}')
    print(f'q.isEmpty(): {q.isEmpty()}')
    print(f'q.isFull(): {q.isFull()}')
    print(f'q.deQueue(): {q.deQueue()}')
    print(f'q: {q.queue}')
    print(f'h: {q.head}, t: {q.tail}')
    print(f'q.Front(): {q.Front()}')
    print(f'q.isEmpty(): {q.isEmpty()}')
    print(f'q.isFull(): {q.isFull()}')
