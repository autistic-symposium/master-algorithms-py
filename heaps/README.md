## heaps

<br>

<p align="center">
<img src="https://github.com/go-outside-labs/master-python-with-algorithms-py/assets/138340846/81f8864a-b997-49b5-9c68-7eabdd02811a" width="80%"/>
</p>



<br> 

* a heap is a binary tree with these properties:
	* it must have all of **its nodes in a specific order**, and
 	* its shape must be **complete** (all the levels of the tree must be completely filled except maybe for the last one and the last level must have the left-most nodes filled, always).
	* a max heap's **root node must** have all its children either **greater than or equal** to its children. a min heap is the opposite. duplicate values are allowed.

* since you always remove the root, insertion and deletion takes `O(log(n))`. the maximum/minimum value in the heap can be obtained with `O(1)` time complexity.
* heaps can be represented with linked lists or queues (arrays).
	* in the case of arrays, the index of the parent `node = [(n-1)/2]`.
<br>

----

### priority queues

* a priority queue is an abstract data type with the following properties:
	1. every item has a priority (usually an integer).
 	2. an item with a high priority is dequeued before an item with low priority.
  	3. two items with an equal priority are dequeued based on their order in the queue.
 
* priority queues can be implemented with a stack, queue, or linked list data structures. however, heaps are the structure that guarantees both insertion and deletion to have time complexity `O(log N)` (while maintaining get_max/get_min at `O(1)`).

<br>

--- 

### min heaps

* a **min heap** is a complete binary tree where each node is smaller than its children (the root is the min element).

* `insert`:
  	- insert the element at the bottom, by finding the most rightmost node and checking its children: if left is empty, insert there, otherwise, insert on right.
  	- then compare this node to each parent, exchanging them until the tree's properties are corret.
  	
* `extract_min`:
  	- first, remove/return the top and then replace the tree's top with its latest element (the bottom most rightmost).
  	- then bubble down, swapping it with one of its children until the min-heap is properly restored
  	- there is no need for order between right and left, so this operation would only take `O(log n)` runtime.

* the code below is an example:

```python
class MinHeap:

    def __init__(self, size):

        self.heapsize = size
        self.minheap = [0] * (size + 1)
        self.realsize = 0

    def add(self, element):

        if self.realsize + 1 > self.heapsize:
            print("Too many elements!")
            return False

        self.realsize += 1
        self.minheap[self.realsize] = element

        index = self.realsize
        parent = index // 2

        while self.minheap[index] < self.minheap[parent] and index > 1:

            self.minheap[parent], self.minheap[index] = self.minheap[index], self.minheap[parent]
            index = parent
            parent = index // 2
    
    def peek(self):

        return self.minheap[1]
    
    def pop(self):

        if self.realsize < 1:
            print("Heap is empty.")
            return False

        else:
            remove_element = self.minheap[1]
            self.minheap[1] = self.minheap[self.realsize]
            self.realsize -= 1
            index = 1

            while index <= self.realsize // 2:

                left_children = index * 2
                right_children = (index * 2) + 1

                if self.minheap[index] > self.minheap[left_children] or \
                   self.minheap[index] > self.minheap[right_children]:

                    if self.minheap[left_children] < self.minheap[right_children]:

                        self.minheap[left_children], self.minheap[index] = self.minheap[index], self.minheap[left_children]
                        index = left_children
                    
                    else:

                        self.minheap[right_children], self.minheap[index] = self.minheap[index], self.minheap[right_children]
                        index = right_children
                else:
                    break

            return remove_element
    
    def size(self):
        return self.realsize
    
    def __str__(self):
        return str(self.minheap[1 : self.realsize + 1])
```

<br>	

--- 

### max heaps

* a **max heap** is a complete binary tree where each node is larger than its children (the root is the max element).

* `insert`:
	* insert the element at the bottom, at the leftmost node.
 	* then compare the node to each parent, exchanging them until the tree's properties are correct.

* `extreact_max`:
	* remove/return the top and then replace the tree's top with its bottom rightmost element.
 	* swap up until the max element is on the top. 

* the code below is an example:

```python
class MaxHeap:
    def __init__(self, heapsize):

        self.heapsize = heapsize
        self.maxheap = [0] * (heapsize + 1)
        self.realsize = 0

    def add(self, element):

        self.realsize += 1
        if self.realsize > self.heapsize:
            print("Too many elements!")
            self.realsize -= 1
            return False

        self.maxheap[self.realsize] = element
        index = self.realsize
        parent = index // 2

        while self.maxheap[index] > self.maxheap[parent] and index > 1:
            self.maxheap[parent], self.maxheap[index] = self.maxheap[index], self.maxheap[parent]
            index = parent
            parent = index // 2
            
    def peek(self):

        return self.maxheap[1]
    
    def pop(self):

        if self.realsize < 1:
            print("Heap is empty.")
            return False
        else:
            remove_element = self.maxheap[1]
            self.maxheap[1] = self.maxheap[self.realsize]
            self.realsize -= 1
            index = 1

            while (index <= self.realsize // 2):

                left_children = index * 2
                right_children = (index * 2) + 1

                if (self.maxheap[index] < self.maxheap[left_children] or self.maxheap[index] < self.maxheap[right_children]):
                    if self.maxheap[left_children] > self.maxheap[right_children]:
                        self.maxheap[left_children], self.maxheap[index] = self.maxheap[index], self.maxheap[left_children]
                        index = left_children
                    else:
                        self.maxheap[right_children], self.maxheap[index] = self.maxheap[index], self.maxheap[right_children]
                        index = right_children
                else:
                    break
            return remove_element
    
    def size(self):
        return self.realsize
    
    def __str__(self):
        return str(self.maxheap[1 : self.realsize + 1])
```

