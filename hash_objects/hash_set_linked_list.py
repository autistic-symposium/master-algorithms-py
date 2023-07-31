#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


class HashSet:

    def __init__(self):
        self.key_range = 131
        self.bucket = [LL_Bucket() for _ in range(self.key_range)]

    def _hash(self, key):
        return key % self.key_range

    def add(self, element: int) -> None:
        bucket_index = self._hash(element)
        self.bucket[bucket_index].insert(element)
    
    def remove(self, element: int) -> None:
        bucket_index = self._hash(element)
        self.bucket[bucket_index].delete(element)

    def contains(self, element: int) -> bool:
        bucket_index = self._hash(element)
        return self.bucket[bucket_index].exists(element)
        

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LL_Bucket:
    def __init__(self):
        # add a pseud head
        self.head = Node(0)

    def insert(self, value):
        if not self.exists(value):
            self.head.next =  Node(value, self.head.next)
        else:
            print(f'node {value} already exists')
        
    def delete(self, value):
        prev = self.head
        current = self.head.next
        while current is not None:
            if current.value == value:
                prev.next = current.next
                return True
            prev = current
            current = current.next
        return False
    
    def exists(self, value):
        current = self.head.next
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False
    
