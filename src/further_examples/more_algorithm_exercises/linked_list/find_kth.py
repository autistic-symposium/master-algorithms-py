#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

''' Find the mth-to-last element of a linked list.
    One option is having two pointers, separated by m. P1 start at the roots (p1 = self.root) and p2 is m-behinf pointer, which is created when p1 is at m. When p1 reach the end, p2 is the node. '''

from linked_list_fifo import Node

class LinkList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.lenght = 0
        
    def addNode(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        if self.tail:
            self.tail.next = node
        self.tail = node
        self.lenght += 1
        
    def removeNode(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.next
            i += 1
        if i == index:    
            if not prev:
                self.head = node.next
            else:
                prev.next = node.next
            self.lenght -= 1
        else:
            print('Index not found')       
        
    def findkth_from_begin(self, k):
        node = self.head
        i = 0
        while node and i < k:
            node = node.next
            i += 1
        while node:
            print(node.value)
            node = node.next
            
    def findkth_to_last(self, k):
        node = self.head
        key = self.lenght - k
        i = 0
        while node and i < key:
            node = node.next
            i += 1
        print(node.value)

    def findkth_to_last_2pointers(self, k):
        node = self.head
        pointer = self.head
        i = 0
        while pointer and i < k:
            pointer = pointer.next
            i += 1
        while pointer:
            node = node.next
            pointer = pointer.next
        print(node.value)
        
    def findkth_to_last_2pointers2(self, k):
        p1 = self.head
        p2 = self.head
        i = 0
        while p1:
            if i >= k: # ---> notice >= not >!
                p2 = p2.next
            p1 = p1.next
            i += 1
        print(p2.value)
           
            
def main():
    ll = LinkList()
    for i in range(1, 11):
        ll.addNode(i)
    # list is 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
    # so 0th from last is 11, 1th to last is 10, 
    # 2th from last is 9!
    
    
    print('Finding from begin...')
    ll.findkth_from_begin(2)    
    print('Finding to last, case 1...')
    ll.findkth_to_last(2) #9  
    print('Finding to last, case 2...')
    ll.findkth_to_last_2pointers(2)  
    print('Finding to last, case 3...')
    ll.findkth_to_last_2pointers2(2)  
              
if __name__ == '__main__':
    main()            

