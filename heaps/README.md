## heaps

<br>

<p align="center">
<img src="https://github.com/go-outside-labs/master-python-with-algorithms-py/assets/138340846/81f8864a-b997-49b5-9c68-7eabdd02811a" width="80%"/>
</p>



<br> 

* heap is a data structure capable of giving you the smallest (or the largest) element in constant time, while adding or removing the smallest (or the largest) element in logarithmic time.

* heaps guarantees both insertion and deletion to have time complexity `O(log N)` (while maintaining get_max/get_min at `O(1)`).

* a heap is a binary tree with these properties:
	* it must have all of **its nodes in a specific order**, and
 	* its shape must be **complete** (all the levels of the tree must be completely filled except maybe for the last one and the last level must have the left-most nodes filled, always).
	* a max heap's **root node must** have all its children either **greater than or equal** to its children. a min heap is the opposite. duplicate values are allowed.

* heaps can be represented with linked lists, queues (arrays), or binary trees.

* in the case of an array heap:
	* the parent node index is given by `n / 2`
	* the left children index is `2 * n`
	* the right children index is `2 * n + 1`
 	* a node is a leaf when its index `> n / 2` 

* common applications of heap are: sort (heap sort), getting the top-k elements, and finding the kth element.

<br>

```python
class Heap:

    def __init__(self):

        self.heap = []

    def heapify(self, n, i):

        largest = i
        left_children = 2 * i + 1
        right_children = 2 * i + 2

        if left_children < n and self.heap[i] < self.heap[left_children]:
            largest = left_children

        if right_children < n and self.heap[largest] < self.heap[right_children]:
            largest = right_children

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(n, largest)


    def insert(self, num):

        size = len(self.heap)

        if size == 0:
            self.heap.append(num)

        else:
            self.heap.append(num)
            for i in range((size // 2) - 1, -1, -1):
                self.heapify(size, i)


    def delete_node(self, num):

        size = len(self.heap)

        i = 0
        for i in range(size):
            if num == self.heap[i]:
                break

        self.heap[i], self.heap[size - 1] = self.heap[size - 1], self.heap[i]

        self.heap.remove(size - 1)

        for i in range((len(self.heap) // 2) - 1, -1, -1):
            self.heapify(len(self.heap), i)
```

<br>

---

### heapify

<br>

* it's cheaper to heapify an array of data (`O(N)`) than create an empty heap and inserting each element (`O(N log(N))`).
	* heapify means create a binary tree and then comparing each nodes with their children (and swapping when necessary).
 	* parents node can simply exchange with their smallest child (so the max number of exchanges is `N/2`) and leaves are left out. 

* python's built-in heap differs from the standard implementation of a heap in two ways:
	* firstly, it uses zero-based indexing, so it stores the root node at index zero instead of the size of the heap.
 	* secondly, the built-in module does not offer a direct way to create a max heap, instead, we must modify the values of each element when inserting in the heap, and when removing it from the heap.

<br>

```python
import heapq

min_heap = [3,1,2]
heapq.heapify(min_heap)

max_heap = [-x for x in min_heap]
heapq.heapify(max_heap)

heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, -5)

min_elem = min_heap[0]
max_elem = -1 * max_heap[0

heapq.heappop(min_heap)
heapq.heappop(max_heap)

size_min_heap = len(min_heap)
size_max_heap = len(max_heap)
```

<br>

----

### priority queues

<br>

* a priority queue is an abstract data type with the following properties:
	1. every item has a priority (usually an integer).
 	2. an item with a high priority is dequeued before an item with low priority.
  	3. two items with an equal priority are dequeued based on their order in the queue.
 
* priority queues can be implemented with a stack, queue, or linked list data structures.

<br>

--- 

### min heaps

<br>

* a **min heap** is a complete binary tree where each node is smaller than its children (the root is the min element).

* `insert`:
  	- insert the element at the bottom, by finding the most rightmost node and checking its children: if left is empty, insert there, otherwise, insert on right.
  	- then compare this node to each parent, exchanging them until the tree's properties are correct.
  	
* `extract_min`:
  	- first, remove/return the top and then replace the tree's top with its latest element (the bottom-most rightmost).
  	- then bubble down, swapping it with one of its children until the min-heap is properly restored
  	- there is no need for order between right and left, so this operation would only take `O(log N)` runtime.

* the code below is an example of an ad-hoc heap class in python.

<br>

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

<br>

* a **max heap** is a complete binary tree where each node is larger than its children (the root is the max element).

* `insert`:
	* insert the element at the bottom, at the leftmost node.
 	* then compare the node to each parent, exchanging them until the tree's properties are correct.

* `extreact_max`:
	* remove/return the top and then replace the tree's top with its bottom rightmost element.
 	* swap up until the max element is on the top. 

* the code below is an example of a max heap class built in python:

  <br>

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

<br>

---


### heap sort

<br>


* the core concept of the heap sort involves constructing a heap from our input and then repeatedly removing the min/max element to sort the array.
  
* the key idea for in-place heap sort involves a balance of these two ideas:
	- building a heap from an unsorted array through a "bottom-up heapification" process, and
 	- using the heap to sort the input array
    
* heapsort traditionally uses a max-heap to sort the array, although a min-heap also works.
  
* this is not a stable sort.

<br>

```python
def heap_sort(self, array) -> None:

      def max_heapify(heap_size, index):
        
            left, right = 2 * index + 1, 2 * index + 2
            largest = index
        
            if left < heap_size and array[left] > array[largest]:
                largest = left
            elif if right < heap_size and array[right] > array[largest]:
                largest = right
            elif largest != index:
                array[index], array[largest] = array[largest], array[index]
                max_heapify(heap_size, largest)

      for i in range(len(lst) // 2 - 1, -1, -1):
            max_heapify(len(array), i)

      for i in range(len(array) - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            max_heapify(i, 0)

      return array
```

<br>

----

### compare two tops


<br>

```python
def compare_two_tops(array) -> int:

        for i in range(len(array)):
            array[i] *= -1

        heapq.heapify(array)

        while len(array) > 1:

            val1 = heapq.heappop(array)
            val2 = heapq.heappop(array)

            if val1 != val2:
                heapq.heappush(array, val1 - val2)

        if array:
            return -heapq.heappop(array)
            
        return 0
```

<br>

----

### find non-overlapping intervals

<br>

* given an array of `intervals[i] = [start_i, end_i]`, return the minimum the non-overlapping intervals

<br>

```python
def non_overlapping_invervals(intervals):
        
        if not intervals:
            return 0

        result = []
        intervals.sort(key=lambda x: x[0])
        heapq.heappush(result, intervals[0][-1])

        for interval in intervals[1:]:

            if result[0] <= interval[0]:
                heapq.heappop(result)
            
            heapq.heappush(result, interval[1])
        
        return len(result)
```

<br>

----

### top k frequent values

<br>

```python
def top_k_frequent_values(list, k):
        
        if k == len(nums):
                return nums

        # hashmap element: frequency
        counter = Counter(nums)
        return heapq.nlargest(k, counter.keys(), key=counter.get)
```

<br>

----

### kth largest element in a stream

<br>

```python
class KthLargest:

    def __init__(self, k, nums):

        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)
        
    def add(self, val: int) -> int:

        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]
```

<br>

----

### kth smallest element in a matrix

<br>

* given an `n x n` matrix where each of the rows and columns is sorted in ascending order, return the `kth` smallest element in the matrix.

<br>

```python
def kth_smallest(matrix, k) -> int:

        min_heap = []

        for row in range(min(k, len(matrix))):
            min_heap.append((matrix[row][0], row, 0))

        heapq.heapify(min_heap)

        while k:

            element, row, col = heapq.heappop(min_heap)
            if col < len(matrix) - 1:
                heapq.heappush(min_heap, (matrix[row][cow + 1], row, col + 1))
            k -= 1
        
        return element
```

<br>



