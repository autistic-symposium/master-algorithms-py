## Linked List

<br>

* unlike an array, a list does not provide constant time access to an index (as it needs to interact through all k elements), however addition and removal of elements are constant time.
* to remove a node you set `prev.next` equal to `node.next`. if it's a double list, you also update `node.next` with `node.next.prev` to `node.prev` (and deallocate the memory).

<br>

### detecting cycles

<br>

* can be done with hash table or the two-pointer technique, where if there is no cycle, the faster pointer (going 2 steps) will stop at the end of the list, but if there is a cycle, the fast pointer will eventually meet the slow pointer (going 1 step). if there is no cycle, the faster pointer takes `N/2` to reach the end of the list (`N` being the length).

<br>

----

### `LinkedListFIFO.py`

<br>

```python
python LinkedListFIFO.py

Linked List FIFO
Add 1: None
Add 2: Nonew
Add 3: None
Length: 3
Find 1: (None, None, 0)
Delete 1: None
Length: 0
Find 1: (None, None, 0)
```

<br>
