## graphs

<br>

* graph is a non-linear data structure consisting of vertices and edges.
  

* graphs can be represented by adjacent matrices, adjacent lists, and hash table of hash tables.

  
* in **undirected graphs**, the edges between any two vertices do not have a direction, indicating a two-way relationship.

  
* in **directed graphs**, the edges between any two vertices are directional.

  
* in **weighted graphs**, each edge has an associated weight. if the sum of the weights of all edges of a cycle is a negative values, it's a negative weight cycle.

  
* the **degree of a vertex** is the number of edges connecting the vertex. in directed, graphs, if the **in-dregree** of a vertex is `d`, there are **d** directional edges incident to the vertex (and similarly, **out-degree** from the vertex).


* with `|V|` the number of vertices and `|E|` is the number of edges, search in a graph (either bfs of dfs) is `O(|V| + |E|)`.

<br>

---

### traversals

<br>

#### breath first search

<br>

* check **[../trees/#breath-first-search](https://github.com/go-outside-labs/master-algorithms-py/blob/master/trees/README.md#tree-traversal-depth-first-search)**

<br>

```python
def bfs(matrix):

  if not matrix:
    return []

  rows, cols = len(matrix), len(matrix[0])
  visited = set()
  directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

  def traverse(i, j):
    queue = deque([(i, j)])
    while queue:
      curr_i, curr_j = queue.popleft()
      if (curr_i, curr_j) not in visited:
        visited.add((curr_i, curr_j))

        for direction in directions:
          next_i, next_j = curr_i + direction[0], curr_j + direction[1]
          if 0 <= next_i < rows and 0 <= next_j < cols:

            queue.append((next_i, next_j))

  for i in range(rows):
    for j in range(cols):
      traverse(i, j)
```

<br>

* or as a class:

<br>

```python

from collections import deque
 

class Graph:

    def __init__(self, edges, n):
 
        self.adj_list = [[] for _ in range(n)]
      
        for (src, dest) in edges:
            self.adj_list[src].append(dest)
            self.adj_list[dest].append(src)
 
 
def bfs(graph, v, discovered):
 
    queue = deque(v)
    discovered[v] = True
 
    while queue:
 
        v = queue.popleft()
        print(v, end=' ')
 
        for u in graph.adj_list[v]:
            if not discovered[u]:
                discovered[u] = True
                queue.append(u)


def recursive_bfs(graph, queue, discovered):
 
    if not queue:
        return
 
    v = queue.popleft()
    print(v, end=' ')
 
    for u in graph.adj_list[v]:
        if not discovered[u]:
            discovered[u] = True
            queue.append(u)
 
    recursive_bfs(graph, queue, discovered)
```

<br>

----

#### depth first search

<br>

* and **[../trees/#depth-first-search](https://github.com/go-outside-labs/master-algorithms-py/blob/master/trees/README.md#tree-traversal-breath-first-search-level-order)**

<br>

```python
def dfs(matrix):
  if not matrix:
    return []

  rows, cols = len(matrix), len(matrix[0])
  visited = set()
  directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

  def traverse(i, j):
    if (i, j) in visited:
      return

    visited.add((i, j))
    for direction in directions:
      next_i, next_j = i + direction[0], j + direction[1]
      if 0 <= next_i < rows and 0 <= next_j < cols:
        traverse(next_i, next_j)

  for i in range(rows):
    for j in range(cols):
      traverse(i, j)
```

<br>

* or as a class:

<br>

```python
from collections import deque

class Graph:

    def __init__(self, edges, n):

        self.adj_list = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adj_list[src].append(dest)
            self.adj_list[dest].append(src)
 

def dfs(graph, v, discovered):
 
    discovered[v] = True           
    print(v, end=' ')              
 
    for u in graph.adj_list[v]:
        if not discovered[u]:       #
            dfs(graph, u, discovered)
 
 

def iterative_dfs(graph, v, discovered):
 
    stack = [v]
 
    while stack:
 
        v = stack.pop()
 
        if discovered[v]:
            continue
 
        discovered[v] = True
        print(v, end=' ')
 
        adj_list = graph.adjList[v]
        for i in reversed(range(len(adj_list))):
            u = adj_list[i]
            if not discovered[u]:
                stack.append(u)
```
  
