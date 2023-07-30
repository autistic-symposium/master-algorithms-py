## trees and graphs

<br>


---

### breath-first search


* similar to pre-order, but work with queue (level order problem)

<br>

---

### depth-first search

* if the depth of the tree is too large, stack overflow might happen, therefore iterative solutions might be better.
* work with stacks

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

- top-down (parameters are passed down to children).


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

### `Tree.py`

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
