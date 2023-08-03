## trees

<br>

### binary trees

<br>

* **binary trees** are trees that have each up to 2 children. a node is called **leaf** if it has no children.
* the **depth of node** is the number of edges from the tree's root node until the node.
* the **height of node** is the number of edges on the longest path between that node and a leaf. the **height of tree** is the height of its root node.
* a **complete tree** is a tree on which every level is fully filled (except perhaps for the last).
* a **full binary tree** has each node with either zero or two children (and no node has only one child).
* a **perfect tree** is both full and complete (it must have exactly 2**k - 1 nodes, where k is the number of levels).

<br>

#### find height

<br>

```python
def height(root):
      if not root:
            return -1
      return 1 + max(height(root.left), height(root.right))
````

<br>

----

### binary search trees

<br>

* **binary search tree** are binary trees where all nodes on the left are smaller than the root, which is smaller than all nodes on the right.
* if a bst is **balanced**, it guarantees `O(log(N))` for insert and search (as we keep the tree's height as `H = log(N)`). common types of balanced trees: **red-black** and **avl**.

<br>

#### predecessor and successor

<br>

```python
def successor(root):
  
  root = root.right
  while root.left:
      root = root.left
      
  return root


def predecessor(root):
  
  root = root.left
  while root.right:
      root = root.right
  
  return root
```

<br>

---

#### search for a value

<br>

```python
def search_bst_recursive(root, val):
        
        if root is None or root.val == val:
            return root
        
        if val > root.val:
            return search_bst_recursive(root.right, val)
        
        else:
            return search_bst_recursive(root.left, val)


def search_bst_iterative(root, val):
        
        node = root
        while node:
            
            if node.val == val:
                return node

            if node.val < val:
                node = node.right

            else:
                node = node.left
        
        return False
```


<br>

* for the recursive solution, in the worst case, the depth of the recursion is equal to the height of the tree. therefore, the time complexity would be `O(h)`. the space complexity is also `O(h)`.
* for an iterative solution, the time complexity is equal to the loop time which is also `O(h)`, while the space complexity is `O(1)`.

<br>

---

#### find lowest common ancestor

<br>

```python
  def lca(self, root, p, q):
        
        node = root
        this_lcw = root.val
        
        while node:
            
            this_lcw = node
            
            if node.val > p.val and node.val > q.val:
                node = node.left
                
            elif node.val < p.val and node.val < q.val:
                node = node.right
                
            else:
                break
        
        return this_lcw
```

<br>

---

#### checking if valid

<br>

```python

def is_valid_bst_recursive(root):
  
          def is_valid(root, min_val=float(-inf), max_val=float(inf)):
            if root is None:
                return True
        
            return (min_val < root.val < max_val) and \
                        is_valid(root.left, min_val, root.val) and \
                        is_valid(root.right, root.val, max_val)
        
      return is_valid(root)


def is_valid_bst_iterative(root):
        
        queue = deque()
        queue.append((root, float(-inf), float(inf)))
        
        while queue:
            node, min_val, max_val = queue.popleft()
            if node:
                if min_val >= node.val or node.val >= max_val:
                    return False
                if node.left:
                    queue.append((node.left, min_val, node.val))
                if node.right:
                    queue.append((node.right, node.val, max_val))
        
        return True
    
    
def is_valid_bst_inorder(root):
        
        def inorder(node):
            if node is None:
                return True
            
            inorder(node.left)
            queue.append(node.val)
            inorder(node.right)
            
        queue = []
        inorder(root)
        for i in range(1, len(queue)):
            if queue[i] <= queue[i-1]:
                return False
            
        return True
```

<br>

---

#### inserting a node

<br>

* the main strategy is to find out a proper leaf position for the target and then insert the node as a leaf (therefore, insertion will begin as a search).
* the time complexity is `O(H)` where `H` is a tree height. that results in `O(log(N))` in the average case, and `O(N)` worst case.

<br>

```python
def bst_insert_iterative(root, val):

  new_node = Node(val)
  this_node = root
  
  while this_node:
    
    if  val > this_node.val:
        if not this_node.right:
          this_node.right = new_node
          return root
        else:
          this_node = this_node.right
    
    else:
        if not this_node.left:
          this_node.left = new_node
          return this_node
        else:
          this_node = this_node.left
        
  return new_node


def bst_insert_recursive(root, val):
        
    if not root:
        return Node(val)

    if val > root.val:
        root.right = self.insertIntoBST(root.right, val)
        
    else:
        root.left = self.insertIntoBST(root.left, val)
        
    return root
```

<br>

---

#### deleting a node

<br>

* deletion is a more complicated operation, and there are several strategies. one of them is to replace the target node with a proper child:
  	- if the target node has no child (it's a leaf): simply remove the node
  	- if the target node has one child, use the child to replace the node
  	- if the target node has two child, replace the node with its in-order successor or predecessor node and delete the node

* similar to the recursion solution of the search operation, the time complexity is `O(H)` in the worst case. according to the depth of recursion, the space complexity is also `O(H)` in the worst case. we can also represent the complexity using the total number of nodes `N`. The time complexity and space complexity will be `O(logN)` in the best case but `O(N)` in the worse case.



<br>

```python
def delete_node(root, key):
        
    if not root:
            return root

    if key > root.val:
            root.right = deleteNode(root.right, key)
      
    elif key < root.val:
            root.left = deleteNode(root.left, key)
      
    else:
        if not (root.left or root.right):
            root = None
          
        elif root.right:
            root.val = successor(root)
            root.right = deleteNode(root.right, root.val)
          
        else:
            root.val = predecessor(root)
            root.left = deleteNode(root.left, root.val)
        
    return root
````

<br>

---

### tree traversal: breath-first search (level-order)

<br>

- iterative solutions use a queue for traversal or find the shortest path from the root node to the target node:
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

### tree traversal: depth-first search

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

---

#### in-order

<br>

- `left -> node -> right`
- in a bst, in-order traversal will be in ascending order (therefore, it's the most frequently used method).

```python
def inorder(self, root):
        if root is None:
            return []
	return inorder(root.left) + [root.val] + inorder(root.right)
````

<br>

---

#### pre-order

<br>

- `node -> left -> right`
- top-down (parameters are passed down to children), so deserialize with a queue.

<br>

```python
def preorder(self, root):
        if root is None:
            return []
	return [root.val] + preorder(root.left) + preorder(root.right)
```


<br>

---

#### post-order

<br>

- `left -> right -> node`
- bottom-up solution (if you know the answer of the children, can you concatenate the answer of the nodes?):
- deletion process is always post-order: when you delete a node, you will delete its left child and its right child before you delete the node itself.
- also, post-order is used in mathematical expressions as it's easier to write a program to parse a post-order expression. using a stack, each time when you meet an operator, you can just pop 2 elements from the stack, calculate the result and push the result back into the stack.

<br>

```python
def postorder(self, root):
        if root is None:
            return []
	return postorder(root.left) + postorder(root.right) + [root.val] 
```



<br>
