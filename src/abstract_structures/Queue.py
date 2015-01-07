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

    def isEmpty(self):
        return not (self.enq + self.deq)

    def size(self):
        return len(self.enq) + len(self.deq)

if __name__ == '__main__':
    q = Queue()

    for i in range(1,10):
        q.enqueue(i)

    assert(q.isEmpty() == False)

    assert(q.size() == 9)

    for i in range(1, 10):
        print q.dequeue()

    assert(q.isEmpty() == True)

