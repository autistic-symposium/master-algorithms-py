## trees

<br>

* a node is called **leaf** if it has no children.
* **binary trees**: each node has up to 2 children.
* **binary search tree**: all nodes on the left are smaller than the root, which is smaller than all nodes on the right.
	* if the bst is **balanced**, it guarantees O(log(n)) for insert and search.
* common types of balanced trees: **red-black** and **avl**.
* a **complete tree** is a tree on which every level is fully filled (except perhaps for the last).
* a **full binary tree** has each node with either zero or two children (and no node has only one child).
* a **perfect tree** is both full and complete (it must have exactly 2**k - 1 nodes, where k is the number of levels).

<br>


---

### breath-first search

<br>

- iterative solutions use a queue for traversal or find the shortest path from the root node to the target node (level order problem)
	- in the first round, we process the root node, in the second round, we process the nodes next to the root node, in the third round, we process the nodes which are two steps from the root node, etc. newly-added nodes will not be traversed immediately but will be processed in the next round.
	- if node X is added to the kth round queue, the shortest path between the root node and X is exactly k.
	- the processing order of the nodes in the exact same order as how they were added to the queue, which is FIFO.

<br>

```python
def bfs(root):

   queue = queue()
   root.marked = True
   queue.enqueue(root)

   while !queue.is_empty():
	node = queue.deque()
	visit(node)
	for n in node_adj:
		n.marked = True
		queue.enque(n)
```
<br>

---

### depth-first search

<br>

- similar to BFS, deep-first search (DFS) can also be used to find the path from the root node to the target node.
- it's a good option for finding the first path (instead of the first path), or if you want to visit every node.
- overall, we only trace back and try another path after we reach the deepest node. as a result, the first path you find in DFS is not always the shortest path.
- we first push the root node to the stack, then we try the first neighbor and push its node to the stack, etc.
- when we reach the deepest node, we need to trace back. when we track back, we pop the deepest node from the stack, which is actually the last node pushed to the stack.
- the processing order of the nodes is exactly the opposite order of how they are added to the stack.
- recursion solutions are easier to implement; however, if the recursion depth is too high, stack overflow might occur. in that case, you might use BFS instead or implement DFS using an explicit stack (i.e., use a while loop and a stack structure to simulate the system call stack).
- if the depth of the tree is too large, stack overflow might happen, therefore iterative solutions might be better.
- work with stacks.

<br>

```python
def dfs(root, visited):
	if root is None:
		return root
	while root.next:
		if root.next not in visited:
			visited.add(root.next)
		return dfs(root.next, visited)
	return False	
```

<br>

#### in-order

- left -> node -> right

```python
def inorder(self, root):
        if root is None:
            return []
	return inorder(root.left) + [root.val] + inorder(root.right)
````

<br>

#### pre-order

- node -> left -> right

```python
def preorder(self, root):
        if root is None:
            return []
	return [root.val] + preorder(root.left) + preorder(root.right)
````

- top-down (parameters are passed down to children), so deserialize with a queue.


<br>

#### post-order

- left -> right -> node

```python
def postorder(self, root):
        if root is None:
            return []
	return postorder(root.left) + postorder(root.right) + [root.val] 
````

- bottom-up solution (if you know the answer of the children, can you concatenate the answer of the nodes?):
- deletion process is always post-order: when you delete a node, you will delete its left child and its right child before you delete the node itself.
- also, post-order is used in mathematical expressions as it's easier to write a program to parse a post-order expression. using a stack, each time when you meet a operator, you can just pop 2 elements from the stack, calculate the result and push the result back into the stack.


<br>

---


### some examples in this dir

<br>

#### `Tree.py`

<br>

```python
> python3 Trees.py


🌴🌴🌴 Testing SimpleTree 🌴🌴🌴
a
	b
		d
		e
	c
		h
		g



🌳🌳🌳 Testing BinaryTree 🌳🌳🌳

🟡 Adding [4, 1, 4, 6, 7, 9, 10, 5, 11, 5] to the tree...
🟢 Printing the tree in preorder...
4
1
6
9
5
5
11
10
7
4

🟢 Searching for node 5: True
❌ Searching for node 15: False
❌ Is root a leaf? False
🟢 Is root full? True
❌ Is the tree balanced? False
❌ Is the tree a binary search tree? False


🎄🎄🎄 Testing BinarySearchTree 🎄🎄🎄

🟡 Adding [4, 1, 4, 6, 7, 9, 10, 5, 11, 5] to the tree...
❌ Item 4 not added as BSTs do not support repetition.
❌ Item 5 not added as BSTs do not support repetition.
🟢 Printing the tree in preorder:
4
1
6
5
7
9
10
11

🟢 Searching for node 5: True
❌ Searching for node 15: False
❌ Is root a leaf? False
🟢 Is root full? True
🟢 Largest node? 11
🟢 Smallest node? 1
❌ Is the tree balanced? False
🟢 Is the tree a binary search tree? True
```

<br>

### `BinaryTree.py`

<br>

* a clean implementation adapted from the class above.

```python
> python3 BinaryTree.py

🌳🌳🌳 Testing BinaryTree 🌳🌳🌳

🟡 Adding [4, 1, 4, 6, 7, 9, 10, 5, 11, 5] to the tree...
🟢 Print the tree preorder: [4, 1, 6, 9, 5, 5, 11, 10, 7, 4]
🟢 Print the tree inorder: [4, 1, 6, 9, 5, 5, 11, 10, 7, 4]
🟢 Print the tree postorder: [4, 1, 6, 9, 5, 5, 11, 10, 7, 4]

🟢 Search for node 5: True
❌ Search for node 15: False
```
