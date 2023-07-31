#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl
#
# Given the root of a binary tree, return all duplicate subtrees.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def find_duplicates(root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

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
