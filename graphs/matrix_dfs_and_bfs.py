#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

'''
Given an m x n 2D binary grid grid which represents a map of 
'1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting 
adjacent lands horizontally or vertically. You may assume all 
four edges of the grid are all surrounded by water.
'''

def num_island_dfs(grid) -> int:
        
        LAND = '1'
        answer = 0

        #######################
        ### go dfs
        #######################
        def dfs(row, col):
          
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != LAND:
                return
            
            grid[row][col] = 'x'
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        #######################
        ## loop through the board
        #######################
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == LAND:
                    answer += 1
                    dfs(i, j)

  
        return answer


def num_island_bfs(grid) -> int:
        
        LAND = '1'
        answer = 0
        queue = collections.deque()

        #######################
        ### go dfs
        #######################
        def bfs(row, col, queue):
            
            delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            
            while queue:
                x, y = queue.popleft()
                
                for dx, dy in delta:
                    
                    px, py = x + dx, y + dy
                    if px < 0 or px >= len(grid) or py < 0 or py >= len(grid[0]) or grid[px][py] != LAND:
                        continue
                        
                    grid[px][py] = 'x'
                    queue.append((px, py))

        #######################
        ## loop through the board
        #######################
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == LAND:
                    answer += 1
                    queue.append((i, j))
                    bfs(i, j, queue)

  
        return answer
