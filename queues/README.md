## queues 

<br>

* first in, first out structures (FIFO), i.e., items are removed at the same order they are added.
* queues can be implemented with two arrays or a dynamic array (linked list), as long as items are added and removed from opposite sides.
* if implemented with a dynamic array, a more efficient solution is to use a circular queue (ring buffer), i.e. a fixed-size array and two pointers to indicate the starting and ending positions. an advantage of circular queues is that we can use the spaces in front of the queue. in a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. but using the circular queue, we can use the space to store new values.
* queues are often used in breath-first search (where you store a list of nodes to be processed) or when implementing a cache.


<br>

----

### examples

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
