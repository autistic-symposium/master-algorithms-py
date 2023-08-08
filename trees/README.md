## trees

<br>

* a tree is a widely used abstract data type that represents a hierarchical structure with a set of connected nodes.
* each node in the tree can be connected to many children, but must be connect to exactly one parent (except for the root node).
* a tree is an undirected and connected acyclic graph and there are no cycle or loops.

<br>

---

### binary trees

<br>

* **binary trees** are trees that have each up to 2 children. a node is called **leaf** if it has no children.
* access, search, remove, insert are all `O(log(N)`. space complexity of traversing balanced trees is `O(h)` where `h` is the height of the tree (while very skewed trees will be `O(N)`.
* the **width** is the number of nodes in a level.
* the **degree** is the nunber of children of a node.
* a **balanced tree** is a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
* a **complete tree** is a tree on which every level is fully filled (except perhaps for the last).
* a **full binary tree** has each node with either zero or two children (and no node has only one child).
* a **perfect tree** is both full and complete (it must have exactly `2**k - 1` nodes, where `k` is the number of levels).

<br>

----

### depth of a binary tree

<br>

* the **depth** (or level) of node is the number of edges from the tree's root node until the node.

<br>

```python
def max_depth(root) -> int:
        
        if root is None:
            return 0
        
        return max(max_depth(root.left) + 1, max_depth(root.right)  + 1)
```

<br>

---

### height of a tree

<br>

* the **height** of a node is the number of edges on the **longest path** between that node and a leaf.
* the **height of tree** is the height of its root node, or the depth of its deepest node.

<br>

```python
def height(root):
      
      if root is none:
            return 0
            
      return 1 + max(height(root.left), height(root.right))
```

---

### tree traversal: breath-first search (level-order)

<br>

* give you all elements **in order** with time `O(log(N)`. used to traverse a tree by level.
  
* iterative solutions use a queue for traversal or find the shortest path from the root node to the target node:
	- in the first round, we process the root node.
 	- in the second round, we process the nodes next to the root node.
  	- in the third round, we process the nodes which are two steps from the root node, etc.
  	- newly-added nodes will not be traversed immediately but will be processed in the next round.
	- if node X is added to the kth round queue, the shortest path between the root node and X is exactly k.
	- the processing order of the nodes in the exact same order as how they were added to the queue (which is FIFO).

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

- deep-first search (DFS) can also be used to find the path from the root node to the target node if you want to visit every node and/or search the deepest paths firsts.
- recursion solutions are easier to implement; however, if the recursion depth is too high, stack overflow might occur. in that case, you might use BFS instead or implement DFS using an explicit stack (i.e., use a while loop and a stack structure to simulate the system call stack). 
- overall, we only trace back and try another path after we reach the deepest node. as a result, the first path you find in DFS is not always the shortest path.
	- we first push the root node to the stack, then we try the first neighbor and push its node to the stack, etc.
	- when we reach the deepest node, we need to trace back.
 	- when we track back, we pop the deepest node from the stack, which is actually the last node pushed to the stack.
	- the processing order of the nodes is exactly the opposite order of how they are added to the stack.

<br>

---

#### in-order

<br>

- `left -> node -> right`
- in a bst, in-order traversal will be sorted in the ascending order (therefore, it's the most frequently used method).
- converting a sorted array to a bst with inorder has no unique solution (in another hadnd, both preorder and postorder are unique identifiers of a bst).

```python
def inorder(root):
        if root is None:
            return []
	return inorder(root.left) + [root.val] + inorder(root.right)

def inorder_iterative(root) -> list:
        
        result = []
        stack = []
        node = root
        
        while stack or node:

            if node:
		stack.append(node)
                node = node.left
            else: 
                node = stack.pop()
                result.append(node.val)
                node = node.right
            
        return result
````

<br>

---

#### pre-order

<br>

- `node -> left -> right`
- top-down (parameters are passed down to children), so deserialize with a queue.

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

---

#### post-order

<br>

- `left -> right -> node`
- bottom-up solution.
- deletion process is always post-order: when you delete a node, you will delete its left child and its right child before you delete the node itself.
- post-order can be used in mathematical expressions as it's easier to write a program to parse a post-order expression. using a stack, each time when you meet an operator, you can just pop 2 elements from the stack, calculate the result and push the result back into the stack.

<br>

```python
def postorder(root):
        if root is None:
            return []
	return postorder(root.left) + postorder(root.right) + [root.val]


def postorder_iterative(root) -> list:
    stack, result = [], []
    node = root
    
    while node or stack:

            while node:
                if node.right:
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
def is_symmetric(root) -> bool:
        
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

### build tree from preorder and inorder

<br>

```python
def build_tree(preorder, inorder) -> Optional[Node]:
        
        def helper(left, right, index_map):
            
            if left > right:
                return None
            
            root = Node(preorder.pop(0))
            index_here = index_map[root.val]

            # this order change from postorder
            root.left = helper(left, index_here - 1, index_map)
            root.right = helper(index_here + 1, right, index_map)
            
            return root
        
        index_map = {value: i for i, value in enumerate(inorder)}
        
        return helper(0, len(inorder) - 1, index_map)
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

#### find if balanced

<br>

```python
def is_balanced(root):
  
    if not root:
      return True

    return abs(height(root.left) - height(root.right)) < 2 and \
            is_balanced(root.left) and is_balanced(root.right)
```

<br>

---

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


