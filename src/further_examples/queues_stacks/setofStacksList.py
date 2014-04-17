from stack import StackList

class SetOfStacksList(object):
    def __init__(self, capacity):
        assert(capacity > 1)
        self.capacity = capacity        
        self.stack_now = []            
        self.old_stacks = []                   
                    
    def _checkIfFull(self):
        return len(self.stack_now) == self.capacity
              
                        
    def _archiveStack(self):
        self.old_stacks.append(self.stack_now)
        self.stack_now = []


    def _popItem(self):
        if self.stack_now:
            return self.stack_now.pop()
        raise Exception('Stack is empty.')    
 
 
    def _sizeStackInUse(self):
        return len(self.stack_now)  


    def numberOfStacksUsed(self):
        if self.stack_now:
            return len(self.old_stacks) + 1
        else:
            return len(self.old_stacks) 


    def seeTop(self):
        if self.stack_now:
            return self.stack_now[-1]
        elif self.old_stacks:
            return self.old_stacks[-1][-1]
        raise Exception('Stack is Empty')
       
            
    def isEmpty(self):
        return not(bool(self.stack_now) or bool(self.old_stacks))
           
           
    def size(self):
        return len(self.stack_now) + self.capacity*len(self.old_stacks)
                        
                        
    def push(self, item):
        self.stack_now.append(item)         
        if self._checkIfFull():
            self._archiveStack()
        
        
    def pop(self):  
        if not self.stack_now:
            if not self.old_stacks:
                raise Exception('Stack is empty')
            else:
                self.stack_now = self.old_stacks.pop()
        return self.stack_now.pop()
        
    def popAt(self, index):
        number_of_stacks = self.size()
        if index < number_of_stacks:
            if index == number_of_stacks - 1 and  self.stack_now:
                return self.stack_now.pop()
            if index < number_of_stacks - 1:
                stack_here = self.old_stacks[index]
                return stack_here.pop()
            raise Exception('Stack at index {} is empty.'.format(index))
        raise Exception('Index larger than the number of stacks.')
            
    def printStacks(self):
        return str(self.old_stacks), str(self.stack_now)

        
def main():
    s1 = SetOfStacksList(3)
    
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
    
    
    s2 = SetOfStacksList(3)
    for i in range(1, 11):
        s2.push(i)
    print(s2.printStacks())
    print(s2.popAt(2))
    
   
if __name__ == '__main__':
    main()           
