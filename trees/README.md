## trees

<br>

* a tree is an undirected and connected acyclic graph with no cycle or loops.

* trees are widely used abstract data type that represents a hierarchical structure with a set of connected nodes.
  
* each node in the tree can be connected to many children, but must be connected to exactly one parent (except for the root node).
  


<br>

---

### binary trees

<br>

* **binary trees** are trees that have up to two children.
  
* `search`, `remove`, and `insert` are all `O(log(N)` runtime.

* the space complexity of traversing balanced trees is `O(h)` where `h` is the height of the tree (while very skewed trees will be `O(N)`).
  
* the **width** of a binary tree is the number of nodes in a level.
  
* the **degree** of a binary tree is the number of children of a node.


<br>

---

### full, complete, and perfect binary trees

<br>

* a **full binary tree** has each node with either zero or two children, i.e., no node has only one child.

* a **complete tree** is a tree on which every level is fully filled (except perhaps for the last).
  
* a **perfect tree** is both full and complete (it must have exactly `2^k - 1` nodes, where `k` is the number of levels).
  
<br>

```python
def is_full(node):

	if node is None:
		return True

	return bool(node.right and node.left) and is_full(node.right) and is_full(node.left)
```

<br>

* a node is called **leaf** if it has no children.

<br>

```python
def is_leaf(node):

	return bool(not node.right and not node.left)
```

<br>


----

### depth of a binary tree

<br>

* the **depth** (or level) of a node is the number of edges from the tree's root node until a certain node.

* the **height of tree** is the height of its root node, or the depth of its deepest node.

<br>

```python
def max_depth(root) -> int:
        
        if root is None:
            return -1
            
      return 1 + max(height(root.left), height(root.right))
```

<br>

---

### balanced trees

<br>

* a **balanced tree** is a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

<br>

```python
def is_balanced(root):

    if root is None:
      return True

    return abs(height(root.left) - height(root.right)) < 2 and \
            is_balanced(root.left) and is_balanced(root.right)
```

<br>

---

### tree traversal: breath-first search (level-order)

<br>

* bfs gives all elements **in order** with time `O(log(N)` and it's used to traverse a tree by level.
  
* iterative solutions use a queue for traversal or find the shortest path from the root node to a target node:
	- in the first round, it processes the root node.
 	- in the second round, it processes the nodes next to the root node.
  	- in the third round, it processes the nodes which are two steps from the root node, etc.
  	- newly-added nodes will not be traversed immediately but will be processed in the next round.
	- if node `X` is added to the `kth` round queue, the shortest path between the root node and `X` is exactly `k`.

<br>

```python
def bfs_iterative(root):

        result = []
        queue = collections.deque([root])
        
        while queue:
    
            node = queue.popleft()
                
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        
        return result

```

<br>

---

### tree traversal: depth-first search

<br>

- dfs is used to find the path from the root node to a target node if you want to visit every node and/or search the deepest paths first.
  
- recursive solutions are easier to implement, however, if the recursion depth is too high, stack overflow might occur.
	- you might want to use bfs instead or implement dfs using an explicit stack (i.e., with a while loop and a stack structure).
  
- dfs only traces back and try another path after it reaches the deepest node. as a result, the first path found in dfs is not always the shortest path:
	- push the root node to the stack.
 	- try the first neighbor and push its node to the stack.
	- when it reaches the deepest node, trace back by popping the deepest node from the stack (the last node pushed). therefore, he processing order of the nodes is exactly the opposite order of how they are added to the stack.

<br>

---

#### in-order

<br>

- `left -> node -> right`

<br>

```python
def inorder_recursive(root):

	if root is None:
            return []

	return inorder_recursive(root.left) + [root.val] + inorder_recursive(root.right)


def inorder_iterative(root):

	node = root
        result, stack = [], []
        
        while stack or node:

            if node:
		stack.append(node)
                node = node.left
            else: 
                node = stack.pop()
                result.append(node.val)
                node = node.right
            
        return result
```

<br>


* we can also build an interator:

<br>

```python
class inorder_iterator:

    def __init__(self, root):
        self.stack = []
        self.left_inorder(root)
        
    def left_inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self.left_inorder(node.right)
        return node.val
        
    def has_next(self) -> bool:
        return len(self.stack) > 0
```

<br>


- in a binary search tree, in-order traversal will be sorted in the ascending order.

- converting a sorted array to a binary search tree with inorder has no unique solution (in another hand, both preorder and postorder are unique identifiers of a bst).

<br>

---

#### pre-order

<br>

- `node -> left -> right`

<br>

```python
def preorder_recursive(root):

        if root is None:
            return []

	return [root.val] + preorder(root.left) + preorder(root.right)


def preorder_iterative(root) -> list:
        
        result = []
        stack = [root]
        
        while stack:
            
            node = stack.pop()
            
            if node:
                result.append(node.val) 
                stack.append(node.right) # not the order (stacks are fifo)
                stack.append(node.left)
            
        return result
```

<br>

* note that preorder dfs looks similar to bfs, but using a stack instead of queue, and calling `node.right` first than `node.left` (as it pops in the right not in the left).

<br>

---

#### post-order

<br>

- `left -> right -> node`
  
- deletion process is always post-order: when you delete a node, you will delete its left child and its right child before you delete the node itself.
  
- post-order can be used in mathematical expressions as it's easier to write a program to parse a post-order expression.
	- using a stack, each time when you meet an operator, you can just pop 2 elements from the stack, calculate the result and push the result back into the stack.

<br>

```python
def postorder(root):

        if root is None:
            return []

	return postorder(root.left) + postorder(root.right) + [root.val]


def postorder_iterative(root):

    node = root
    stack, result = [], []
    
    while node or stack:

            while node:
                stack.append(node.right)
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            
            if stack and node.right == stack[-1]:
                stack[-1] = node
                node = node.right

            else:
                result.append(node.val)
                node = None
                
    return result
```

<br>


----

### is same tree?

<br>

```python
def is_same_trees(p, q):

        if not p and not q:
            return True
        
        if (not p and q) or (not q and p):
            return False
        
        if p.val != q.val:
            return False
        
        return is_same_trees(p.right, q.right) and is_same_trees(p.left, q.left)
````

<br>

---

### is symmetric?

<br>

```python
def is_symmetric(root):
        
        stack = [(root, root)]
        
        while stack:
            
            node1, node2 = stack.pop()
            
            if (not node1 and node2) or (not node2 and node1):
                return False
            
            if node1 and node2:

		if node1.val != node2.val:
                     return False

		stack.append([node1.left, node2.right])
		stack.append([node1.right, node2.left])
        
        return True


def is_symmetric_recursive(root) -> bool:
            
        def helper(node1, node2):
                if (not node1 and node2) or \
                   (not node2 and node1) or \
                   (node1 and node2 and node1.val != node2.val):
                        return False
                
                if (not node1 and not node2):
                        return True
                
                return helper(node1.left, node2.right) and helper(node2.left, node1.right)
            
        return helper(root.left, root.right)
```

<br>

---

### lowest common ancestor

<br>

```python
def lowest_common_ancestor(root, p, q):

    stack = [root]
    parent = {root: None}
    
    while p not in parent or q not in parent:

        node = stack.pop()
        if node:
            parent[node.left] = node
            parent[node.right] = node
            stack.append(node.left)
            stack.append(node.right)

    ancestors = set()
    while p:
        ancestors.add(p)
        p = parent[p]

    while q not in ancestors:
        q = parent[q]
            
    return q
```

<br>

---

### has path sum?

<br>


```python
def has_path_sum(root, target_sum) -> bool:
    
        def transverse(node, sum_here=0):
            
            if not node:
                return sum_here == target_sum
            
            sum_here += node.val
            
            if not node.left:
                return transverse(node.right, sum_here)
            if not node.right:
                return transverse(node.left, sum_here)
            else:   
                return transverse(node.left, sum_here) or transverse(node.right, sum_here)
    
        if not root:
            return False
        
        return transverse(root)
```

<br>

---

### build tree from inorder with preorder or postorder

<br>

* building with preorder:

<br>

```python
def build_tree(preorder, inorder):
        
        def helper(left, right, index_map):
            
            if left > right:
                return None

            node = preorder.pop(0) # this order change from postorder
            root = Node(node.val) 
            index_here = index_map[node.val]

            root.left = helper(left, index_here - 1, index_map) # this order change from postorder
            root.right = helper(index_here + 1, right, index_map)
            
            return root
        
        index_map = {value: i for i, value in enumerate(inorder)}
        
        return helper(0, len(inorder) - 1, index_map)
```

<br>

* build with postorder:

<br>

```python
def build_tree(left, right, index_map, postorder):
            
        if left > right:
                return None

        node = postorder.pop() # this order change from preorder
        root = Node(node.val)  
        index_here = index_map[node.val]

        root.right = build_tree(index_here + 1, right, index_map, postorder) # this order change from preorder
        root.left = build_tree(left, index_here - 1, index_map, postorder)
            
        return root


def build_tree(inorder, postorder):

        index_map = {val: i for i, value in enumerate(inorder)}
        return fill_tree(0, len(inorder) - 1, index_map, postorder)
```


<br>

---

### return number of unival subtrees

<br>

* a unival subtree means all nodes of the subtree have the same value

<br>

```python
def count_unival(root) -> int:
        
        global count = 0
        
        def dfs(node):
            if node is None:
                return True
            
            if dfs(node.left) and dfs(node.right):
                if (node.left and node.left.val != node.val) or \
                    (node.right and node.right.val != node.val):
                         return False
                self.count += 1
                return True
            
            return False

        dfs(root)
        return count
```

<br>

---

### successors and precessors

<br>

```python

def successor(root):
  
  root = root.right
  while root:
      root = root.left
      
  return root


def predecessor(root):
  
  root = root.left
  while root:
      root = root.right
  
  return root
```

<br>


----

### binary search trees

<br>

* **binary search tree** are binary trees where all nodes on the left are smaller than the root, which is smaller than all nodes on the right.
  
* if a bst is **balanced**, it guarantees `O(log(N))` for insert and search (as we keep the tree's height as `h = log(N)`).
  
* common types of balanced trees are **red-black** and **avl**.



<br>

---

### insert a node

<br>

* the main strategy is to find out a proper leaf position for the target and then insert the node as a leaf (therefore, insertion will begin as a search).

* the time complexity is `O(h)` where `h` is a tree height. that results in `O(log(N))` in the average case, and `O(N)` worst case.

<br>

```python
def bst_insert_iterative(root, val):

  node = root
  while node:
    
    if val > node.val:
        if not node.right:
          node.right = Node(val)
          break
        else:
          node = node.right
    
    else:
        if not node.left:
          node.left = Node(val)
          break
        else:
          node = node.left
        
  return root


def bst_insert_recursive(root, val):
        
    if root is None:
        return Node(val)

    if val > root.val:
        root.right = self.bst_insert_recursive(root.right, val)
        
    else:
        root.left = self.bst_insert_recursive(root.left, val)
        
    return root
```

<br>


---

### delete a node

<br>

* deletion is a more complicated operation, and there are several strategies.

* one of them is to replace the target node with a proper child:
  	- if the target node has no child (it's a leaf): simply remove the node
  	- if the target node has one child, use the child to replace the node
  	- if the target node has two child, replace the node with its in-order successor or predecessor node and delete the node

* similar to the recursion solution of the search operation, the time complexity is `O(h)` in the worst case.
  
* according to the depth of recursion, the space complexity is also `O(h)` in the worst case. we can also represent the complexity using the total number of nodes `N`.
  
* the time complexity and space complexity will be `O(log(N))` in the best case but `O(N)` in the worse case.


<br>

```python
def successor(root):
   
    root = root.right
    while root.left:
         root = root.left
    return root.val


def predecessor(root):
  
    root = root.left
    while root.right:
         root = root.right
    return root.val


def delete_node(root, key):
        
    if root is None:
         return root

    if key > root.val:
         root.right = delete_node(root.right, key)
      
    elif key < root.val:
            root.left = delete_node(root.left, key)
      
    else:
        if not (root.left or root.right):
            root = None
          
        elif root.right:
            root.val = successor(root)
            root.right = delete_node(root.right, root.val)
          
        else:
            root.val = predecessor(root)
            root.left = delete_node(root.left, root.val)
        
    return root
```

<br>

---

### search for a value

<br>

* for the recursive solution, in the worst case, the depth of the recursion is equal to the height of the tree. therefore, the time complexity would be `O(h)`. the space complexity is also `O(h)`.
  
* for an iterative solution, the time complexity is equal to the loop time which is also `O(h)`, while the space complexity is `O(1)`.

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
        
        while root:
            
            if root.val == val:
                break
            if root.val < val:
                root = root.right
            else:
                root = root.left
        
        return root
```


<br>

---

### find successor of two nodes inorder

<br>

```python
def find_successor(node1, node2):

    successor = None

    while node1:

        if node1.val <= node2.val:
            node1 = node1.right
        else:
            successor = node1
            node1 = node1.left

    return successor
```

<br>


---

### convert sorted array to bst

<br>

* note that there is no unique solution.

<br>

```python
def convert_sorted_array_to_bst(nums):

      def helper(left, right):
        
            if left > right:
                return None

            p = (left + right) // 2

            root = Node(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)

            return root
        
      return helper(0, len(nums) - 1)
```

<br>


---

### lowest common ancestor for a bst

<br>

```python
def lowest_common_ancestor(root, p, q):

        node, result = root, root
        
        while node:
            
            result = node
            
            if node.val > p.val and node.val > q.val:
                node = node.left
            elif node.val < p.val and node.val < q.val:
                node = node.right
            else:
                break
        
        return result
```

<br>

---

### checking if bst is valid

<br>

```python
def is_valid_bst_iterative(root):
        
        queue = deque((root, float(-inf), float(inf)))
        
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


def is_valid_bst_recursive(root, min_val=float(-inf), max_val=float(inf)):
            
        if root is None:
            return True
        
        return (min_val < root.val < max_val) and \
                  is_valid_bst_recursive(root.left, min_val, root.val) and \
                  is_valid_bst_recursive(root.right, root.val, max_val)
    
    
def is_valid_bst_inorder(root):
        
        def inorder(node):
            if node is None:
                return True
            
            inorder(node.left)
            stack.append(node.val)
            inorder(node.right)
            
        stack = []
        inorder(root)
  
        for i in range(1, len(stack)):
            if queue[i] <= queue[i - 1]:
                return False
            
        return True
```

<br>

