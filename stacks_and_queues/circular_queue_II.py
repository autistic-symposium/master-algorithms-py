#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

## implement a circular queue


class CircularQueue:

    def __init__(self, k: int):
        self.head = -1
        self.tail = -1
        self.size = k
        self.queue = [None] * self.size
        
    def enQueue(self, value: int) -> bool:

        if self.isFull():
            return False

        if self.isEmpty():
            head = 0;

        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = value

        return True

    def deQueue(self) -> bool:

        if self.isEmpty():
            return False

        if self.head == self.tail:
            self.head = -1
            self.tail = -1
            return True
        
        self.head = (self.head + 1) % self.size

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]
        
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail]
        
    def isEmpty(self) -> bool:
        return self.head == -1

    def isFull(self) -> bool:
        return (self.tail + 1) % self.size == self.head
        

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
