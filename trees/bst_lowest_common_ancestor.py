#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

  def lca(self, root, p, q):
        
        node = root
        this_lcw = root.val
        
        while node:
            
            this_lcw = node
            
            if node.val > p.val and node.val > q.val:
                node = node.left
                
            elif node.val < p.val and node.val < q.val:
                node = node.right
                
            else:
                break
        
        return this_lcw
