#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

class Queue():

    def __init__(self):
        self._in = []
        self._out = []

    ######################
    #   Private methods
    ######################
    def _transfer_in_to_out(self):
        while self._in:
            self._out.append(self._in.pop())
    
    def __repr__(self):
        if not self._out:
            self._transfer_in_to_out()
        
        return f'{self._out}'


    ######################
    #  Properties
    ######################
    @property
    def size(self):
        return len(self._in) + len(self._out)
    
    @property
    def peek(self):
        if not self._out:
            self._transfer_in_to_out()
        if self._out:
            return self._out[-1]
        else:
            print('❌ Queue is empty, cannot peek.')
    
    @property
    def is_empty(self):
        return not (bool(self._in) or bool(self._out))

    ######################
    #   Public methods
    ######################
    def enqueue(self, item):
        self._in.append(item)

    def dequeue(self):
        if not self._out:
            while self._in:
                self.out.append(self._in.pop())

        if self._out:
             self._out.pop()
        else:
            print('❌ Queue is empty, cannot dequeue.')


if __name__ == '__main__':

    queue = Queue()
    print(f"Is the queue empty? {queue.is_empty}")
    print("Adding 1 to 10 in the queue...")
    for i in range(1, 11):
        queue.enqueue(i)
    
    print(f"Queue: {queue}")
    print(f"\nQueue size: {queue.size}")
    print(f"Queue peek : {queue.peek}")
    print(f"Is the queue empty? {queue.is_empty}")
    print(f"\nDequeue...")
    queue.dequeue()
    print(f"Queue: {queue}")
    print(f"\nQueue size: {queue.size}")
    print(f"Queue peek: {queue.peek}")
    print(f"Is the queue empty? {queue.is_empty}")

