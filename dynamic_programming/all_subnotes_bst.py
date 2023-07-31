#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def all_possible_bst(start, end, memo):

        result = []
        if start > end:
            result.append(None)
            return result
        
        if (start, end) in memo:
            return memo[(start, end)]

        for i in range(start, end + 1):
            left = all_possible_bst(start, i-1, memo)
            right = all_possible_bst(i+1, end, memo)

            for l in left:
                for r in right:
                    root = TreeNode(i, l, r)
                    result.append(root)

        memo[(start, end)] = result
        return result


def generateTrees(n) -> List[Optional[TreeNode]]:

    memo = {}
    return all_possible_bst(1, n, memo)
