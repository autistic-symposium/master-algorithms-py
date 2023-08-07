#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

from collections import deque
 

class Graph:

    def __init__(self, edges, n):
 
        self.adj_list = [[] for _ in range(n)]
      
        for (src, dest) in edges:
            self.adj_list[src].append(dest)
            self.adj_list[dest].append(src)
 
 
def bfs(graph, v, discovered):
 
    q = deque()
    discovered[v] = True
 
    q.append(v)
 
    while q:
 
        v = q.popleft()
        print(v, end=' ')
 
        for u in graph.adj_list[v]:
            if not discovered[u]:
                discovered[u] = True
                q.append(u)


def recursive_bfs(graph, q, discovered):
 
    if not q:
        return
 
    v = q.popleft()
    print(v, end=' ')
 
    for u in graph.adj_list[v]:
        if not discovered[u]:
            discovered[u] = True
            q.append(u)
 
    recursive_bfs(graph, q, discovered)
  
