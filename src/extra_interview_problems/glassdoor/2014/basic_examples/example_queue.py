#!/usr/bin/python

import Queue

q = Queue.Queue()

for i in range(10):
    q.put(i)

for i in range(10):
    print q.get(i)
