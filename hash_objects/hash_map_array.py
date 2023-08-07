#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


class Bucket:

    def __init__(self):
        self.bucket = []

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1
    
    def put(self, key, value):
        found = False
        for i, k in enumerate(self.bucket):
            if key == k[0]:
                self.bucket[i] = (key, value)
                found = True
                break
        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        for i, k in enumerate(self.bucket):
            if key == k[0]:
                # del is an O(N) operation, as we would copy all the i: elements
                # to make it O(1) we could swap the element we want to remove
                # with the last element in the bucket
                del self.bucket[i]


class HashMap:

    def __init__(self, key_space):
        self.key_space = key_space
        self.table = [Bucket() for _ in range(self.key_space)]
        
    def put(self, key: int, value: int):
        hash_key = key % self.key_space
        self.table[hash_key].put(key, value)

    def get(self, key: int):
        hash_key = key % self.key_space
        return self.table[hash_key].get(key)

    def remove(self, key: int):
        hash_key = key % self.key_space
        self.table[hash_key].remove(key)
        


