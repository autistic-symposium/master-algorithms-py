#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

'''
Design a map that allows you to do the following:
- Maps a string key to a given value.
- Returns the sum of the values that have a key with a prefix equal to a given str.
'''

class Node:
    
    def __init__(self):
        self.children = {}
        self.score = 0


class MapSum:

    def __init__(self):
        self.map = {}
        self.root = Node()

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        
        node = self.root
        node.score += delta
        for c in key:
            node = node.children.setdefault(c, Node())
            node.score += delta

    def sum(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return 0
            node = node.children[c]
          
        return node.score
        
