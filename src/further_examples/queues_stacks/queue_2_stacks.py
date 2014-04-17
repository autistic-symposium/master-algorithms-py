class MyQueue(object):
    def __init__(self):
        self.enq = []
        self.deq = []
        
    def enqueue(self, item):
        self.enq.append(item)    
        
    def _addStacks(self):
        aux = []
        if self.enq:
            while self.enq:
                aux.append(self.enq.pop())
        aux.extend(self.deq) 
        self.deq = aux
    
    def dequeue(self):
        self._addStacks()
        if self.deq:
            return self.deq.pop()         
        raise Exception('Cannot "deque": Queue is empty')
        
    def peek(self):
        if self.deq:
            return self.deq[-1]
        elif self.enq:
            return self.enq[0]
        raise Exception('Cannot "peek": Queue is empty')
   
    def isEmpty(self):
        return not (bool(self.enq) or bool(self.deq))
    
    def size(self):
        return len(self.enq) + len(self.deq)

    def printQueue(self):
        self._addStacks()
        if self.deq:
            aux = str(self.deq).strip('[]') 
            return 'Front --> ' + aux +' <-- Back' 
        else:
            raise Exception('Cannot "printQueue": Queue is empty')
          

def main():
    q = MyQueue()
    for i in range(1, 11):
        q.enqueue(i)
        print(q.printQueue())    
    assert(q.peek() == 1)
    assert(q.isEmpty() == False)
    assert(q.size() == 10)    
        
    for i in range (1, 10):
        q.dequeue()
        print(q.printQueue()) 
      
    
if __name__ == '__main__':
    main()
