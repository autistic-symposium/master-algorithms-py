#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


class MedianFinder:

    def __init__(self):
        
        self.min_heap = []
        self.max_heap = []

        
    def addNum(self, num: int) -> None:
        
        min_heap, max_heap = self.min_heap, self.max_heap
        
        if len(min_heap) < len(max_heap):
            heappush(min_heap, num)
            
        else:
            heappush(max_heap, -num)
            
        if max_heap and min_heap and -max_heap[0] > min_heap[0]:
            
            heappush(max_heap, -heappop(min_heap))
            heappush(min_heap, -heappop(max_heap))
        
        
    def findMedian(self):
        
        min_heap, max_heap = self.min_heap, self.max_heap
        
        if len(min_heap) < len(max_heap):
            return -max_heap[0]
        
        return (min_heap[0] - max_heap[0]) / 2
