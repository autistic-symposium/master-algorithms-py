#!/usr/bin/python3
# steinkirch at gmail.com
# astro.sunysb.edu/steinkirch

class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Stack(object):
    def __init__(self):
        self.top = None

    def push(self, item):
        node = Node(item)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top:
            node = self.top
            self.top = node.next            
            return node.value
        raise Exception('Stack is empty.')

    def isEmpty(self):
        return bool(self.top)
    
    def seeTop(self):
        if self.top:
            return self.top.value
        raise Exception('Stack is empty.')
    
    def size(self):
        node = self.top
        count = 0
        while node:
            count +=1
            node = node.next
        return count
   
            
class StackList(list):
    def __init__(self):
        self.items = []
     
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if self.items:
            return self.items.pop()
        raise Exception('Stack is empty.')
       
    def seeTop(self):
        if self.items:
            return self.items[-1]
        raise Exception('Stack is empty.')
     
    def size(self):
        return len(self.items)
        
    def isEmpty(self):
        return bool(self.items)
   
        
def main():
    s1 = StackList()
    print(s1.isEmpty())
    for i in range(1, 10):
        s1.push(i)
    print(s1.isEmpty())
    print(s1.size())
    print(s1.seeTop())
    s1.pop()
    print(s1.size())
    print(s1.seeTop())       
    
    
    s2 = Stack()
    print(s2.isEmpty())
    for i in range(1, 10):
        s2.push(i)
    print(s2.isEmpty())
    print(s2.size())
    print(s2.seeTop())
    s2.pop()
    print(s2.size())
    print(s2.seeTop())    


if __name__ == '__main__':
    main()           
