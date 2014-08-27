#!/usr/bin/python

__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"

''' an (inefficient) class for a queue '''

class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return bool(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

    def __repr__(self):
        return '{}'.format(self.items)



if __name__ == '__main__':
    queue = Queue()
    print("Is the queue empty? ", queue.isEmpty())
    print("Adding 0 to 10 in the queue...")
    for i in range(10):
        queue.enqueue(i)
    print("Queue size: ", queue.size())
    print("Queue peek : ", queue.peek())
    print("Dequeue...", queue.dequeue())
    print("Queue peek: ", queue.peek())
    print("Is the queue empty? ", queue.isEmpty())
    print(queue)