## linked list

<br>

* like arrays, a linked list is used to represent sequential data. it's a linear collection of data elements (nodes) whose order is not given by their physical placement in memory (as opposed to arrays where data is stored in sequential blocks of memory). instead, each element contains an address of the next element.

<br>

```python
class Node:

  def __init__(self, val, next=None):
      self.val = val
      self.next = next
```

<br>

* unlike an array, a linked list does not provide constant time access to an index (as it needs to interact through all `k` elements), however addition and removal of elements are constant time (`O(1)`).
  * if you need to add or delete a node frequently, a linked list could be a good choice.
  * if you need to access an element by index often, an array might be a better choice than a linked list. 

* linked lists can be of the following types:
  * **singled linked list**: a linked list where each node points to the next node and the last node points to `None`.
  * **doubly linked list**: a linked list where each node has two pointers, `next` and `prev`. the `prev` pointer of the first node and the `next` pointer of the last node point to `None`.
  * **circular linked list**: a singly linked list where the past node points back to the first node. if it's doubly, the `prev` pointer of the first node points to the last node, and the `next` pointer of the last node points to the first node.

* each node in a singly-linked list contains a value and a reference field to link to the next node. the head node (first node) usually represents the whole list.
  * nodes can be added at the beginning, head needs to be updated (`current -> head` and `head = current`).
  * to remove a node you set `prev.next` equal to `node.next`. if it's a double list, you also update `node.next` with `node.next.prev` to `node.prev` (and deallocate the memory).
 
* adding a sentinel/dummy node at the head and/or tail might help handle many edge cases where operations have to be performed at the head or the tail.
  * the presence of dummy nodes ensures that operations will never be done on the head or the tail (removing the need of conditional checks to deal with `None` pointers). the only extra steps is that they need to be removed at the end of the operation.
  * examples are LRU cache (where sentinel nodes are used as pseudo-head and pseudo-tail) and tree level order traversal (where sentinel nodes are used to mark level end).

* two pointers can be used to solve several problems:
  * getting the kth from last node: have two pointers, where one is `k` nodes ahead of the other, when the node ahead reaches the end, the other node is `k` behind.
  * detecting cycles: have two pointers, where one pointer increments twice as much as the other. if the two pointers meet, there is a cycle. if there is no cycle, the faster pointer takes `N/2` to reach the end of the list (`N` being the length).
  * getting in the middle node: have two pointers, where one pointer increments twice as much as the other. when the faster node reaches the end of the list, the slower node will be at the middle.
 

<br>

<p align="center">
<img src="https://github.com/go-outside-labs/master-python-with-algorithms-py/assets/138340846/046045d6-f749-4322-a11b-3dc48322fed0" width="70%" align="center" style="padding:1px;border:1px solid black;">
</p>


<br>


----

### detecting cycles

<br>

```python
def has_cycle(head) -> bool:
        
        if not head:
            return False
        
        p1 = head
        p2 = head.next
        
        while p1 != p2:
            
            if not p1 or not p2 or not p2.next:
                return False
            
            p1 = p1.next
            p2 = p2.next.next
        
        return True
```

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

   prev = None
   curr = head
        
   while curr:
       next_temp = curr.next     // save the pointer for the next node so we can continue the loop
       curr.next = prev          // revert the list
       prev = curr               // save for the next node revert
       curr = next_temp          // receive the pointer for the next node so we can continue the loop

   return prev
```


<br>

---

### removing elements

<br>

* given a head of a linked list and a value, how to remove all the nodes of the list that have that value?

<br>

```python
def delete_node_without_head(node):

  node.val = node.next.val
  node.next = node.next.next
```
<br>
  
* this problem is easy if one has to delete a node in the middle, as all you need to do is loop until the predecessor node and change the pointers.

* however, if the node to be deleted is in the head of the list, the best way is to use a sentinel node. sentinel nodes are widely used in trees and linked lists as pseudo-heads, pseudo-tails, markers of level end, etc. they are purely functional and usually do not hold any data. their main purpose is to standardize the process (by making the list never empty or headless).


<br>

```python
def remove_elements(head, val):
        
        sentinel = ListNode(0)
        sentinel.next = head
        prev, node = sentinel, head

        while node:
            if node.val == val:
                prev.next = node.next
            else:
                prev = node
            node = node.next
                
        return sentinel.next
```

<br>


---

### remove kth node

<br>

```python
def remove_kth_node(self, head, n):
  
        if head is None or head.next is None:
            return None

        # find the length of the list
        node, length = head, 0
        while node:
            node = node.next
            length += 1

        # if n is the entire list, remove head
        if n == length:
            return head.next
    
        # loop to kth element
        node, i = head, 0
        while i <= length - n:
            node = node.next
            i += 1

        # remove the kth element
        node.next = node.next.next
                
        return head
```

<br>

----

### doubly linked lists

<br>

* in doubly linked lists, a node has a `previous` field.
  
* when it comes to add and delete operations, extra attention is needed when you want to delete or insert at the beginning or at the end of the list.



<br>

----

### swap every two nodes

<br>

```python
def swap_pairs(head):
  
      if not head or not head.next:
          return head

      first_node = head
      second_node = head.next

      first_node.next = swap_pairs(second_node.next)
      second_node.next = first_node

      return second_node
```

<br>

----


### rotate list by k

<br>

* the nodes in the list are already linked, so the rotation means:
  * to close the linked list in the ring
  * to break the ring after the new tail and in front of the new head

* the new head will be at `n - k`, and the new tail will be at `n - k - 1` (found with `n - k % n - 1`).

<br>

```python3
def rotate_list_by_k(head, k):
        
    if head is None:
        return head

    # get the size of the list
    end, n = head, 1
    while end.next:
        end = end.next
        n += 1

    # rotate
    end.next = head
    new_end, i = head, 0
    while i < n - (k % n) - 1:     
        new_end = new_end.next
        i += 1

    # remove cycle
    new_head = new_end.next
        
    return new_head
```
