#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

# Given the root of a binary tree, return all duplicate subtrees.


def find_duplicates(root: Optional[Node]) -> list[Optional[Node]]:

        result = []
        counter = {}

        def traverse(node):
            if not node:
                return ""

            rep = ("(" + traverse(node.left) + ")" + \
                            str(node.val) + "(" +  \
                            traverse(node.right) + ")")
            
            if rep in counter:
                counter[rep] += 1
            else:
                counter[rep] = 1

            if counter[rep] == 2:
                result.append(node)
            
            return rep
        
        traverse(root)
        return result
