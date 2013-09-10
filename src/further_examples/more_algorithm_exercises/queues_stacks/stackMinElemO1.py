from stack import Stack, Node, StackList


class StackMinElen(Stack):
    def __init__(self):
        self.top = None
        self.mins = []
              
    def printMin(self):
        if self.mins:
            return self.mins[-1]
        raise Exception('Stack is empty.')


    def pop(self):
        if self.top:
            self.mins.pop()
            node = self.top
            self.top = node.next      
            return node.value    
        raise Exception('Stack is empty.')

    
    def push(self, item): 
        if self.top:
            min_so_far = self.mins[-1]
            if min_so_far > item:
                self.mins.append(item)
            else:
                self.mins.append(min_so_far)
        else:
            self.mins.append(item)       
        node = Node(item)
        node.next = self.top
        self.top = node
        
        
        

class StackListMinElen(StackList):
    def __init__(self):
        self.items = []
        self.mins = []

    def printMin(self):
        if self.mins:
            return self.mins[-1]
        raise Exception('Stack is Empty')

    def push(self, item):     
        self.items.append(item)  
        if self.mins:
            if self.mins[-1] > item:
                self.mins.append(item)
            else:
                self.mins.append(self.mins[-1])
        else:
            self.mins.append(item)
                                                          
    def pop(self):
        if self.items:
            self.mins.pop()
            return self.items.pop()
        raise Exception('Stack is Empty')




        
def main():
    s1 = StackListMinElen()
    l1 = [4, 2, 6, 3, 1, 5]
    for i in l1:
        s1.push(i)  
    print('Min: ', s1.printMin())
    print('Pop: ', s1.pop())
    print('Min: ', s1.printMin())
    print('Pop: ', s1.pop())
    print('Min: ', s1.printMin())
    print('Pop: ', s1.pop())        
    print('Min: ', s1.printMin())
    print('Pop: ', s1.pop())        
    print('Min: ', s1.printMin())
    print('Pop: ', s1.pop())        
    print('Min: ', s1.printMin())   


    s2 = StackMinElen()
    l1 = [4, 2, 6, 3, 1, 5]
    for i in l1:
        s2.push(i)  
    print('Min: ', s2.printMin())
    print('Pop: ', s2.pop())
    print('Min: ', s2.printMin())
    print('Pop: ', s2.pop())
    print('Min: ', s2.printMin())
    print('Pop: ', s2.pop())        
    print('Min: ', s2.printMin())
    print('Pop: ', s2.pop())        
    print('Min: ', s2.printMin())
    print('Pop: ', s2.pop())        
    print('Min: ', s2.printMin())   



if __name__ == '__main__':
    main()           
