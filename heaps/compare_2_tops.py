#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


'''
You are given an array of integers stones where 
stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, 
we choose the heaviest two stones and smash them together. 
Suppose the heaviest two stones have weights x and y with 
x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone 
of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. 
'''

def last_stone(stones) -> int:

        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)

        while len(stones) > 1:

            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)

            if stone_1 != stone_2:
                heapq.heappush(stones, stone_1 - stone_2)

        if stones:
            return -heapq.heappop(stones)
            
        else:
            return 0
          
