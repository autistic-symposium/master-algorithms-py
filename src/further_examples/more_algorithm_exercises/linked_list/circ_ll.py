#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail


''' Build a class for a circular linked list and implement a function to see whether
    a linked list is circular'''

from linked_list_fifo import Node, LinkList

class Node(object):
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


class CircLinkList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.lenght = 0
    
    def addNode(self, value):
        node = Node(value, self.head)
        if not self.head:
            self.head = node
        if self.tail:
           self.tail.next = node
        self.tail = node
        self.lenght += 1
        
    def printList(self):
        size = self.lenght
        node = self.head
        i = 0
        while i < size:
            print(node.value)
            node = node.next   
            i += 1
        
        
 
def isCircularll(ll):
    p1 = ll.head
    p2 = ll.head
    
    while p2 and p2.next:
        p1 = p1.next
        p2 = p2.next.next
        
        if p1 == p2:
            return True
    return False

def main():
    ll = CircLinkList()
    for i in range(10):
        ll.addNode(i)
    ll.printList()
    
    print(isCircularll(ll))
    
    ll2 = LinkList()
    for i in range(10):
        ll2.addNode(i)
    ll2.printList() 

    print(isCircularll(ll2)) 
    
                   
if __name__ == '__main__':
    main()
