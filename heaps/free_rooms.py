#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


'''
Given an array of meeting time intervals intervals 
where intervals[i] = [starti, endi], return the 
minimum number of conference rooms required.
'''

def min_meeting_rooms(intervals):
        
        if not intervals:
            return 0

        free_rooms = []

        intervals.sort(key= lambda x: x[0])

        heapq.heappush(free_rooms, intervals[0][-1])

        for i in intervals[1:]:

            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)
            
            heapq.heappush(free_rooms, i[1])
        
        return len(free_rooms)
