#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

def height(root):
      if not root:
            return -1
      return 1 + max(height(root.left), height(root.right))
  
