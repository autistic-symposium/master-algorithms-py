from stack import Stack, Node

class SetOfStacks(object):
    def __init__(self, capacity):
        assert(capacity > 1)
        self.capacity = capacity        
        self.stack_now = None
        self.stack_now_size = 0               
        self.old_stacks = []
                    
                    
    def _checkIfFull(self):
        return self.stack_now_size == self.capacity
        

    def _addStack(self):       
        self.stack_now =  Stack()
        self.stack_now_size = 0
        
                        
    def _archiveStack(self):
        self.old_stacks.append(self.stack_now)
        self.stack_now = None
        self.stack_now_size = 0   

     
    def _popItem(self):
        if self.stack_now.top:
            value = self.stack_now.top.value
            if self.stack_now.top.next:
                node = self.stack_now.top
                self.stack_now.top = self.stack_now.top.next              
            else:
                self.stack_now = [] 
            return value
        raise Exception('Stack is empty.')    
    

    def numberOfStacksUsed(self):
        if self.stack_now:
            return len(self.old_stacks) + 1
        else:
            return len(self.old_stacks) 


    def seeTop(self):
        if self.stack_now:
            return self.stack_now.top.value
        elif self.old_stacks:
            return self.old_stacks[-1].top.value
        raise Exception('Stack is Empty')
       
            
    def isEmpty(self):
        return not (bool(self.stack_now) or bool(self.old_stacks))
           
    
    def _sizeStackInUse(self):
        return self.stack_now_size


    def size(self):
        return self._sizeStackInUse() + self.capacity*len(self.old_stacks)
                        
 
    def push(self, item):
        if not self.stack_now:
             self._addStack()
        
        node = Node(item)
        node.next = self.stack_now.top
        self.stack_now.top = node         
        
        self.stack_now_size += 1
        
        if self._checkIfFull():
            self._archiveStack()
        
        
    def pop(self):  
        if not self.stack_now:
            if not self.old_stacks:
                raise Exception('Stack is empty')
            else:
                self.stack_now = self.old_stacks.pop()
                self.stack_now_size = self.capacity - 1
                self._popItem()
        else:
            self._popItem() 
            if self.stack_now:
                self.stack_now_size -= 1
            else:
                self.stack_now_size = 0
            

        
def main():
    s1 = SetOfStacks(3)
    
    print(s1.numberOfStacksUsed())
    print(s1.isEmpty())
    print(s1.size())
    
    s1.push(1)
    print('Push item 1')
    print(s1.numberOfStacksUsed())
    print(s1.seeTop())
    print(s1.isEmpty())
    print(s1.size())
    
    s1.push(2)
    s1.push(3)
    print('Push item 2 and 3')
    print(s1.numberOfStacksUsed())
    print(s1.seeTop())
    print(s1.isEmpty())
    print(s1.size())
    
    s1.push(4)
    print('Push item 4')
    print(s1.numberOfStacksUsed())
    print(s1.seeTop())
    print(s1.isEmpty())
    print(s1.size())   
    
    s1.push(5)
    print('Push item 5')
    print(s1.numberOfStacksUsed())
    print(s1.seeTop())
    print(s1.isEmpty())
    print(s1.size())  
    
    s1.pop()
    print('Pop item 5')
    print(s1.numberOfStacksUsed())
    print(s1.seeTop())
    print(s1.isEmpty())
    print(s1.size())  
    
    s1.pop()
    print('Pop item 4')
    print(s1.numberOfStacksUsed())
    print(s1.seeTop())
    print(s1.isEmpty())
    print(s1.size())  
    
    s1.pop()
    s1.pop()
    print('Pop item 3 e 2')
    print(s1.numberOfStacksUsed())
    print(s1.seeTop())
    print(s1.isEmpty())
    print(s1.size())  
    
    s1.pop()
    print('Pop item 1')
    print(s1.numberOfStacksUsed())
    print(s1.isEmpty())
    print(s1.size())  
    
    
    
   
if __name__ == '__main__':
    main()           
