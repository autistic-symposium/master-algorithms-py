## heaps


<br>

* a heap is a binary tree with two properties: it must have all of its nodes in a specific order and its shape must be complete (all the levels of the tree must be completely filled except maybe for the last one and the last level must have the left-most nodes filled, always).
* a heap's root node must have all its children either greater than or equal to its children.
* since you always remove the root, insertion and deletion takes O(log(n)).
* duplicate values are allowed.
* a **min heap** is a complete binary tree where each node is smaller than its children (the root is the min element). two key operations are:
 	- insert: always by the element at the bottom, at the most rightmost post
  	- extract_min: the minimum element is always on top, and removing it is the trickiest part:
  	  	1. remove and swap it with the last element (the bottom most rightmost)
  	 	2. the bubble down, swapping it with one of its children until the min-heap is properly restored (there is no order between right and left and it takes O(log n) time.
* a heap could also be represented with a queue (array). in this case, the index of the parent node = [(n-1)/2].
* a priority queue is a queue of data structures with some additional properties:
	1. every item has a priority (usually an integer)
 	2. an item with a high priority is dequeued before an item with low priority
  	3. two items with an equal priority are dequeued based on their order in the queue   
 

<br>
