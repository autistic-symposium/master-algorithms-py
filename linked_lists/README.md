## Linked Lists

<br>

* each node in a singly-linked list contains a value and a reference field to link to the next node. the head node (first node) usually represents the whole list.

* unlike an array, a linked list does not provide constant time access to an index (as it needs to interact through all k elements), however addition and removal of elements are constant time.
  * if you need to add or delete a node frequently, a linked list could be a good choice.
  * if you need to access an element by index often, an array might be a better choice than a linked list. 

* nodes can be added at the beginning, head needs to be updated (`current -> head` and `head = current`).

* to remove a node you set `prev.next` equal to `node.next`. if it's a double list, you also update `node.next` with `node.next.prev` to `node.prev` (and deallocate the memory).

<br>

<p align="center">
<img src="https://github.com/go-outside-labs/master-python-with-algorithms-py/assets/138340846/046045d6-f749-4322-a11b-3dc48322fed0" width="70%" align="center" style="padding:1px;border:1px solid black;">
</p>


<br>

--- 

### detecting cycles

<br>

* cycles in a linked list can be detected by using a hash table or with the two-pointer technique.
  
* if there is no cycle, the faster pointer (going 2 steps) will stop at the end of the list, but if there is a cycle, the fast pointer will eventually meet the slow pointer (going 1 step).

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

---

### removing elements

<br>

* given a head of a linked list and a value, how to remove all the nodes of the list that have that value?

* this problem is easy if one has to delete a node in the middle, as all you need to do is loop until the predecessor node and change the pointers.

* however, if the node to be deleted is in the head of the list, the best way is to use a sentinel node. sentinel nodes are widely used in trees and linked lists as pseudo-heads, pseudo-tails, markers of level end, etc. they are purely functional and usually do not hold any data. their main purpose is to standardize the process (by making the list never empty or headless).

* examples are LRU cache (where sentinel nodes are used as pseudo-head and pseudo-tail) and tree level order traversal (where sentinel nodes are used to mark level end).

<br>

```python
def remove_elements(head, val):
        
        sentinel = ListNode(0)
        sentinel.next = head
        prev, current = sentinel, head

        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
                
        return sentinel.next
```

<br>

----

### doubly linked lists

<br>

* in doubly linked lists, a node has a `previous` field.
  
* when it comes to add and delete operations, extra attention is needed when you want to delete or insert at the beginning or at the end of the list.



<br>

