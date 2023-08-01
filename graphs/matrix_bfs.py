#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

'''
You are given an m x n grid rooms initialized with these three possible values.

* -1 A wall or an obstacle.
* 0 A gate.
* INF Infinity means an empty room (2^31 - 1 = 2147483647 to represent INF)

Fill each empty room with the distance to its nearest gate. 
If it is impossible to reach a gate, it should be filled with INF.
'''

def matrix_bfs(rooms: list[list[int]]) -> None:
        
        m = len(rooms)
        if m == 0:
           return rooms
        n = len(rooms[0])
        
        GATE = 0
        EMPTY = 2147483647
        DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))

        q = collections.deque()

        for i in range(m):
            for j in range(n):
                
                if rooms[i][j] == GATE:
                    q.append((i, j))

        while q:

            row, col = q.popleft()

            for (x, y) in DIRECTIONS:

                r = row + x
                c = col + y

                if (r < 0) or (c < 0) or (r >= m) or (c >= n) or rooms[r][c] != EMPTY:
                    continue

                rooms[r][c] = rooms[row][col] + 1
                q.append((r, c))            
