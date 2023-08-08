## queues 

<br>

* queues are **first in, first out (FIFO) abstract structures** (*i.e.*, items are removed at the same order they are added) that can be implemented with two arrays or a dynamic array (linked list), as long as items are added and removed from opposite sides.

* queues support **enqueue** (add to one end) and **dequeue** (remove from the other end, or tail).

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

#### with an array

<br>

* to build a ring with a fixed size array, any of the elements could be considered as the head.

* to enqueue, you loop the queue with the tail index until find a `None` (even if it has to loop back):

<br>

```python
while self.queue[self.tail] is not None:
      self.tail += 1 
      if self.tail == self.size:
            self.tail = 0
self.queue[self.tail] = value
```

<br>

* to dequeue, you simply pop the head value:

<br>

```python
value = self.queue[self.head]
self.queue[self.head] = None
self.head += 1
```

<br>
  
* as long as we know the length of the queue, we can instantly locate its tails based on this formula:

<br>

```
tail_index = (head_index + current_length - 1) % size
```

<br>

* there is one occasion when `tail` index is set to zero:
   * when the enqueue operation adds to the last position in the array and tail has to loop back (`self.tail == self.size`).

* there are two occasions when `head` index is set to zero:
   * when the queue is checked as empty
   * when the dequeue operation popped the last element in the array and head has to loop back (`self.head == self.size`).
 
<br>

```python
class CircularQueue:

    def __init__(self, size):
        self.head = 0
        self.tail = 0
        self.size = size
        self.queue = [None] * self.size
        
    def enqueue(self, value: int) -> bool:
        if self.is_full():
            return False

        if self.is_empty():
            self.head = 0
        
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
        return self.queue[self.head] or False
        
    def rear(self) -> int:
        return self.queue[self.tail] or False
        
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

* another version used only one index (for `head`) and calculates the tail with the equation:

<br>

```python
(self.head + self.count - 1) % self.size
````

<br>

* and the next tail with:

<br>

```python
(self.head + self.count) % self.size
```

<br>

* and the next `head` is always given by:

<br>

```python
(self.head + 1) % self.size
```

<br>

* * in this example we also implement the methods `is_empty` and `is_full` using an extra counter variable `self.count` that can be compared to `self.size` or `0` and used to validate `rear` and `front`.

<br>

```python
class CircularQueue:

    def __init__(self, size):
        self.head = 0
        self.count = 0
        self.queue = [0] * size
        self.size = size

    def _get_tail(self):
        return (self.head + self.count - 1) % self.size

    def _get_next_tail(self):
        return (self.head + self.count) % self.size

    def _get_next_head(self):
        return (self.head + 1) % self.size

    def enqueue(self, value: int) -> bool:

        if self.is_empty():
          return False
          
        self.queue[self._get_next_tail()] = value
        self.count += 1
      
        return True

    def dequeue(self) -> bool:

        if self.is_empty():
          return False
          
        self.head = self._get_next_head()
        self.count -= 1
      
        return True

    def Front(self) -> int:
        if self.is_empty():
          return False
        
      return self.queue[self.head]

    def Rear(self) -> int:
        if self.is_empty():
          return False
          
        return self.queue[self._get_tail()]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size
```

<br>



#### with linked lists

<br>

* a simpler and more natural implementation, as the size of the queue is not "artificial" like before.

* note that this queue is not thread-safe: the data structure could be corrupted in a multi-threaded environment (as race-condition could occur). to mitigate this problem, one could add the protection of a lock.

<br>

```python
class Node:
    def __init__(self, value, next=None):
        
        self.value = value
        self.next = next


class Queue:

    def __init__(self, size):
        
        self.size = size
        self.count = 0
        self.head = None
        self.tail = None
        
    def enqueue(self, value: int) -> bool:
        
        if self.is_full():
            return False
            
        if self.is_empty():
            self.head = self.tail = Node(value)
        
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        
        self.count += 1
        
        return True

    def dequeue(self) -> bool:
        
        if self.is_empty():
            return False
             
        self.head = self.head.next
        self.count -= 1
        
        return True

    def front(self) -> int:
        if self.is_empty():
            return False
        return self.head.value

    def rear(self) -> int:
        if self.is_empty():
            return False
        return self.tail.value
    
    def is_empty(self) -> bool:
        return self.count == 0

    def is_full(self) -> bool:
        return self.count == self.size
```

<br>

---

### a stream with rate limiter

<br>

```python
class Logger:

    def __init__(self):
        self.msg_set = set()
        self.msg_queue = deque()
        
    def print_message(self, timestamp, message) -> bool:
        
        while self.msg_queue:
            msg, msg_timestamp = self.msg_queue[0]
            if timestamp - msg_timestamp >= 10:
                self.msg_queue.popleft()
                self.msg_set.remove(msg)
            else:
                break
        
        if message not in self.msg_set:
            self.msg_set.add(message)
            self.msg_queue.append((message, timestamp))
            return True
            
        return False
```

<br>

---

### moving average

<br>

* given a stream of integers and a window size, the moving average in the sliding window can be calculated with a queue:

<br>

```python

class MovingAverage:

    def __init__(self, size: int):
        
        self.queue = []
        self.size = size
        

    def next(self, val: int) -> float:
        
        self.queue.append(val)
        
        if len(self.queue) > self.size:
            self.queue.pop(0)
        
        return sum(self.queue) / len(self.queue)
```
