#!/usr/bin/env python

__author__ = "bt3"


class Queue(object):
    def __init__(self):
        self.enq = []
        self.deq = []

    def enqueue(self, value):
        self.enq.append(value)

    def dequeue(self):
        if not self.deq:
            while self.enq:
                self.deq.append(self.enq.pop())
        return self.deq.pop()

if __name__ == '__main__':
    q = Queue()

    for i in range(1,10):
        q.enqueue(i)

    for i in range(1, 10):
        print q.dequeue()