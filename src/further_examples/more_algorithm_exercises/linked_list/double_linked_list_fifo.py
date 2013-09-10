#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

''' Implement a double-linked list, which is very simple, we just need inherets from a Linked List Class and  add an attribute for prev.'''

from linked_list_fifo import LinkList

class dNode(object):
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
        self.prev = None    # THIS IS THE EXTRA ATTRIBUTE FOR DOUBLE L
        self.children = None    # THIS IS NOT USED HERE, IS EXAMPLES WITH MANY LL INSIDE LLs
        
class dLinkList(LinkList):
 
    def addNode(self, value):
        node = dNode(value)
        if not self.head:
            self.head = node
        if self.tail:
            node.prev = self.tail   # ADD THIS WHEN DOUBLE L
            self.tail.next = node
        self.tail = node
        self.length += 1
    
            
    def printListInverse(self): # THIS IS THE EXTRA METHOD FOR DOUBLE L
        node = self.tail
        while node:
            print(node.value)
            node = node.prev
 
                        
        

from collections import Counter

def main():
  
    ll = dLinkList()
    for i in range(1, 10):
        ll.addNode(i)
    print('Printing the list...')
    ll.printList()
    print('Now, printing the list inversely...')
    ll.printListInverse()
    
  
    
if __name__ == '__main__':
    main()
