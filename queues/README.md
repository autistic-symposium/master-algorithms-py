## queues 

<br>

* queues are **first in, first out (FIFO) abstract structures** (*i.e.*, items are removed at the same order they are added) that can be implemented with two arrays or a dynamic array (linked list), as long as items are added and removed from opposite sides.

* queues support **enqueue** (add to the end one end) and **dequeue** (remove from the other end, or tail).

* if implemented with a dynamic array, a more efficient solution is to use a circular queue (ring buffer), *i.e.*, a fixed-size array and two pointers to indicate the starting and ending positions.
    * an advantage of circular queues is that we can use the spaces in front of the queue.
    * in a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. but using the circular queue, we can use the space to store new values.
 
* queues are often used in **breath-first search** (where you store a list of nodes to be processed) or when implementing a cache.


<br>

---

### designing a circular queue

<br>

* a circular queue can be built with either arrays or linked lists (nodes).

<br>

#### using arrays

<br>

* to build a ring with a fixed size array, any of the elements could be considered as the head.
  
* as long as we know the length of the queue, we can instantly locat its tails based on this formula:

<br>

```
tail_index = (head_index + queue_length - 1) % queue_capacity
```

<br>


```python
class CircularQueue:

    def __init__(self, k: int):
        self.head = 0
        self.tail = 0
        self.size = k
        self.queue = [None] * self.size
        
    def enqueue(self, value: int) -> bool:

        if value is None:
            return False
            
        if self.is_full():
            return False

        if self.is_empty():
            self.heard = 0
        
        while self.queue[self.tail] is not None:
            self.tail += 1 
            if self.tail == self.size:
                self.tail = 0
    
        self.queue[self.tail] = value
        return True

    def dequeue(self) -> bool:

        if self.is_empty():
            return False

        value = self.queue[self.head]
        self.queue[self.head] = None
        self.head += 1

        if self.head == self.size:
            self.head = 0

        return True

    def front(self) -> int:
        return self.queue[self.head] or -1
        
    def rear(self) -> int:
        return self.queue[self.tail] or -1
        
    def is_empty(self) -> bool:
        for n in self.queue:
            if n is not None:
                return False
        return True

    def is_full(self) -> bool:
        for n in self.queue:
            if n is None:
                return False
        return True
```

<br>

#### using linked lists

<br>

* note that this queue is not thread-safe: the data structure could be corrupted in a multi-threaded environment (as race-condition could occur). to mitigate this problem, one could add the protection of a lock.

<br>

```python
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
```


<br>


