#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

import heapq

min_heap = [3,1,2]
heapq.heapify(min_heap)

max_heap = [-x for x in min_heap]
heapq.heapify(max_heap)
