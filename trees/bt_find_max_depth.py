#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

def max_depth(root: Optional[Node]) -> int:
        
        if root is None:
            return 0
        
        return max(max_depth(root.left) + 1, max_depth(root.right)  + 1)
