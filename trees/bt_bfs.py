#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


def level_order(root: Optional[Node]) -> list[list[int]]:
        
        if root is None:
            return []
        
        queue = collections.deque()
        queue.append(root)
        result = []
        
        while queue:
            
            this_level = []
            
            for _ in range(len(queue)):
                
                current = queue.popleft()
                
                if current:
                    this_level.append(current.val)
                    queue.append(current.left)
                    queue.append(current.right)
            
            if this_level:
                result.append(this_level)
        
        return result
