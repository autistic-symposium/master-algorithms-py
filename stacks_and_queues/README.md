## stacks and queues

<br>

### queues

<br>

* queues can be implemented with two arrays or a dynamic array (linked list).
* if implemented with a dynamic array, a more efficient solution is to use a circular queue (ring buffer), i.e. a fixed-size array and two pointers to indicate the starting and ending positions.
* an advantage of circular queues is that we can use the spaces in front of the queue. in a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. but using the circular queue, we can use the space to store new values.


<br>

----

### `Queues.py`

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

### `stack.py`

<br>

```python
python3 stack.py

Testing Stack...

Stack: [12, 13, 14, 15, 16, 17, 18, 19, 20]
Stack size: 9
Stack peek: 20
Stack is empty: False
Stack min: 12

Popping...
20
19
18
17
16
Stack: [12, 13, 14, 15]
```
