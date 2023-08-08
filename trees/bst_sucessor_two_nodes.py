#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


def find_successor(root, p):

    successor = None

    while root:

        if root.val <= p.val:
            root = root.right
        else:
            successor = root
            root = root.left

    return successor
