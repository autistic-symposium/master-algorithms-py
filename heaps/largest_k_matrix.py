#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

'''
You are given an m x n binary matrix mat of 1's (representing soldiers) 
and 0's (representing civilians). The soldiers are positioned in front 
of the civilians. That is, all the 1's will appear to the left of
all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered 
from weakest to strongest.
'''


 def k_weakest_row(self, mat, k):

        m = len(mat)
        n = len(mat[0])

        def binary_search(row):

            low = 0
            high = n

            while low < high:

                mid = (low + high) // 2
                if row[mid] == 1:
                    low = mid + 1
                else:
                    high = mid

            return low


        pq = []
        for i, row in enumerate(mat):

            strength = binary_search(row)
            entry = (-strength, -i)
            if len(pq) < k or entry > pq[0]:
                heapq.heappush(pq, entry)
            if len(pq) > k:
                heapq.heappop(pq)
            
        indexes = []
        while pq:
            strength, i = heapq.heappop(pq)

            indexes.append(-i)
        
        return indexes[::-1]
