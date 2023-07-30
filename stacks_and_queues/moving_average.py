'''
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.
'''

class MovingAverage:

    def __init__(self, size: int):
        self.queue = []
        self.size = size
        

    def next(self, val: int) -> float:
        
        self.queue.append(val)
        
        if len(self.queue) > self.size:
            self.queue.pop(0)
        
        return sum(self.queue) / len(self.queue)
    
