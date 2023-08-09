## tries

<br>

* tries, also called prefix tree, are a variant of n-ary tree in which characters are stored in each node. they are used to make searching and storing more efficient, as search, insert, and remove are `O(m)` (`m` being the length of the string).

* tries structures can be represented by arrays and maps or trees.
    * comparying with a hash table, they lose in terms of time complexity, as hash table insert is usually `O(1)` (worst case `O(log(N))`, and trie's are `O(m)` (where `m` is the maximum length of a key).
    * however, trie wins in terms of space complexity. both `O(m * N)` in theory, but tries can be much smaller as there will be a lot of words that have similar prefix.

  

* each trie node represents a string (a prefix) and each path down the tree represents a word. note that not all the strings represented by trie nodes are meaningful. the root is associated with the empty string.
    * the `*` nodes (`None` nodes) are often used to indicate complete words (usually represented by a special type of child) or a boolean flag that terminates the parent node.
    * a node can have anywhere from 1 through `alphabet_size + 1` child.

* tries can be used to store the entire english language for quick prefix lookup. they are also widely used on autocompletes, spell checkers, and ip routing (longest prefix matching).



<br>

```python
class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['$'] = None
        
    def match(self, seq, prefix=False):
        node = self.root
        for c in seq:
            if c not in node:
                return False
            node = node[c]
        return prefix or ('$' in node)
        
    def search(self, word: str) -> bool:
        return self.match(word)
        
    def starts_with(self, prefix: str) -> bool:
        return self.match(prefix, True)
```

<br>

----

### insertion

<br>

* similar to a bst, when we insert a value to a trie, we need to decide which path to go depending on the target value we insert.
  
* the root node needs to be initialized before you insert strings.

<br>


---

### search

<br>

* all the descendants of a node have a common prefix of the string associated with that node, so it should be easy to search if there are any words in the trie that starts with the given prefix.
  
* we go down the tree depending on the given prefix, once we cannot find the child node, the search fails.
  
* we can also search for a specific word rather than a prefix, treating this word as a prefix and searching in the same way as above.
  
* if the search succeeds, we need to check if the target word is only a prefix of words in the trie or if it's exactly a word (for example, by adding a boolean flag).

<br>

#### bfs

<br>

```python
def level_orders(root):

    if root is None:
        return []

    result = []
    queue = collections.deque([root])

    while queue:
        level = []
        
        for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                queue.extend(node.children)
            result.append(level)
        
  return result
```

<br>

#### post order

<br>

```python
def postorder(self, root: 'Node'):
        
    if root is None:
        return []

    stack, result = [root, ], []

    while stack:
            
      node = stack.pop()
            
      if node is not None:
          result.append(node.val)
              
      for c in node.children:
          stack.append(c)
        
    return result[::-1]
```

<br>

#### pre-order

<br>

```python
def preorder(root: 'Node'):
        
        if root is None:
            return []
        
        stack, result = [root, ], []

        while stack:
                
            node = stack.pop()
            result.append(node.val)
            stack.extend(node.children[::-1])
            
        return result
```

<br>

----

### max depth

<br>

```python
def max_depth_recursive(root):

    if root is None:
            return 0

    if root.children: is None:
            return 1

    height = [max_depth_recursive(children) for children in root.children]
    
   return max(height) + 1


def max_depth_iterative(root):

        stack, depth = [], 0
  
        if root is not None:
            stack.append((1, root))

        while stack:
            
            this_depth, node = stack.pop()
          
            if node is not None:
              
                depth = max(depth, this_depth)
                for c in node.children:
                    stack.append((this_depth + 1, c))
        
        return depth
```
