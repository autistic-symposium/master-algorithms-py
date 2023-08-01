## queues 

<br>

* queues are **first in, first out structures (FIFO)** (i.e., items are removed at the same order they are added) that can be implemented with two arrays or a dynamic array (linked list), as long as items are added and removed from opposite sides.

  
* if implemented with a dynamic array, a more efficient solution is to use a circular queue (ring buffer), i.e. a fixed-size array and two pointers to indicate the starting and ending positions.
    * an advantage of circular queues is that we can use the spaces in front of the queue.
    * in a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. but using the circular queue, we can use the space to store new values.
 
    
* queues are often used in breath-first search (where you store a list of nodes to be processed) or when implementing a cache.


<br>

---

### designing a circular queue

<br>

* a circular queue can be built with either arrays or linked lists (nodes). to build a ring with a fixed size array, any of the elements could be considered as the head.
* as long as we know the length of the queue, we can instantly locat its tails based on this formula:

```
tail_index = (head_index + queue_length - 1) % queue_capacity
```

<br>

* here is an example of an implementation using a "fixed-sized" array (sort of) using arrays:

<br>

```python
class CircularQueue:

    def __init__(self, k: int):
        self.head = -1
        self.tail = -1
        self.size = k
        self.queue = [None] * self.size
        
    def _get_next_position(self, end) -> int:
        return (end + 1) % self.size
        
    def enQueue(self, value: int) -> bool:

        if self.is_full():
            return False

        if self.is_empty() :
            self.head = 0;
        
        self.tail = self._get_next_position(self.tail)
        self.queue[self.tail] = value

        return True

    def deQueue(self) -> bool:

        if self.is_empty():
            return False

        if self.head == self.tail:
            self.head = -1
            self.tail = -1
            return True
        
        self.head = self._get_next_position(self.head)

        return True

    def front(self) -> int:
        if self.is_empty():
            return -1
        return self.queue[self.head]
        
    def rear(self) -> int:
        if self.is_empty():
            return -1
        return self.queue[self.tail]
        
    def is_empty(self) -> bool:
        return self.head == -1

    def is_full(self) -> bool:
        return self._get_next_position(self.tail) == self.head
```

<br>

* and here is a much clear example using a linked list:

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

* note that this queue is not thread-safe: the data structure could be corrupted in a multi-threaded environment (as race-condition could occur). to mitigate this problem, one could add the protection of a lock.


<br>

----

### some examples in this directory

<br>

#### `queues.py`

<br>

```python
> python3 queues.py

🧪 Testing Queue...
Is the queue empty? True
Adding 1 to 10 in the queue...
Queue: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

Queue size: 10
Queue peek : 1
Is the queue empty? False

Dequeue...
Queue: [10, 9, 8, 7, 6, 5, 4, 3, 2]

Queue size: 9
Queue peek: 2
Is the queue empty? False


🧪 Testing Priority Queue...
Priority Queue: [(-4, 1, Item 4), (-1, 0, Item 1), (-3, 2, Item 3)]
Pop: Item 4
Priority Queue: [(-3, 2, Item 3), (-1, 0, Item 1)]
```

<br>
