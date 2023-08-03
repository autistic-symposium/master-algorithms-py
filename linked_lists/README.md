## Linked List

<br>

* each node in a singly-linked list contains a valye and a reference fiedl to link to the next node. the head node (first node) usually represents the whole list.

* unlike an array, a linked list does not provide constant time access to an index (as it needs to interact through all k elements), however addition and removal of elements are constant time.

* nodes can be added at the beginning, head needs to be update (`current -> head` and `head = current`).

* to remove a node you set `prev.next` equal to `node.next`. if it's a double list, you also update `node.next` with `node.next.prev` to `node.prev` (and deallocate the memory).

<br>


--- 

### detecting cycles

<br>

* can be done with hash table or the two-pointer technique, where if there is no cycle, the faster pointer (going 2 steps) will stop at the end of the list, but if there is a cycle, the fast pointer will eventually meet the slow pointer (going 1 step).

* if there is no cycle, the faster pointer takes `N/2` to reach the end of the list (`N` being the length).

<br>

----

### reversing the list

<br>

* keep track of the original head node and the new head node (for instance, with two pointers).

<br>

```python
def reverse_list(head):

  if head is None:
      return head
        
  final_head = head
        
  while head.next:
      
      new_node = head.next
      head.next = new_node.next
      new_node.next = final_head
      final_head = new_node
        
  return final_head
```


<br>

<br>

----

### some exercises in this dir

<br>

#### `LinkedListFIFO.py`

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
