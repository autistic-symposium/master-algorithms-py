#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

class Stack(object):
    ''' define the stack class '''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, items):
        self.items.append(items)

    def pop(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

   
        

def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.size())    
    print(stack.peek())   
    print(stack.pop())  
    print(stack.peek())    


if __name__ == '__main__':
    main()
