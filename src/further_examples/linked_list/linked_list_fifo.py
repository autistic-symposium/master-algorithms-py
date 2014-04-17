#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

''' A class for a linked list that has the nodes in a FIFO order (such as a queue)'''


class Node(object):
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
        
class LinkList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def addNode(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        if self.tail:
            self.tail.next = node
        self.tail = node
        self.length += 1
    
    def printList(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next
     
    def addInOrder(self, item):
        new_node = Node(item)
        node = self.head
        previous = None
        stop = False
        while node and not stop:
            if node.value > item:
                stop = True
            else:
                previous = node
                node = node.next

        if not previous:
            new_node.next = self.head
            self.head = new_node
        else:
            new_node.next = node 
            previous.next = new_node
    
            
    
    def deleteNode(self, index):
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
            self.length -= 1
        else:
            print('Index not found!')


    def deleteNodeIfOrdered(self, item):
        node = self.head
        previous = None
        found = False
        while node and not found:
            if node.value == item:
                found = True
            else:
                previous = node
                node = node.next
        
        if found:
            if not previous:
                self.head = node.next
            else:
                previous.next = node.next
        else:
            print('Node not found!')            
            
                       
    def removeDupl(self):
        prev = None
        node = self.head
        aux_dict = Counter()      
        while node:           
            value_here = node.value
            if aux_dict[value_here] == 0:
                aux_dict[value_here] = 1
            else:              
                if prev == None:
                    self.head = node.next
                else:
                    prev.next = node.next
                self.length -= 1              
            prev = node
            node = node.next   
            
    def removeDupl_no_buf(self):
        node = self.head
        while node:
            pivot = node.value
            pointer = node.next
            prev = node
            while pointer:
                value_here = pointer.value
                if value_here == pivot:
                    prev.next = pointer.next
                    self.length -= 1 
                prev = pointer
                pointer = pointer.next
            node = node.next      
                    
    def searchIfOrdered(self, item):
        node = self.head
        found = False
        stop = False
        while node and not found and not stop:
            if node.value  == item:
                found = True
            else:
                if node.value > item:
                    stop = True
                else:
                    node = node.next
        return found                        
    
    
    
    
        

from collections import Counter

def main():
    
    ll = LinkList()
    for i in range(1, 10):
        ll.addNode(i)
        ll.addNode(i+1)
    print('Linked List with duplicates:')    
    ll.printList()
    print('Length before deleting duplicate is: ', ll.length)
    ll.removeDupl()
    ll.printList()
    print('Lenght after deleting duplicates is: ', ll.length)   
    
    ll = LinkList()
    for i in range(1, 10):
        ll.addNode(i)
        ll.addNode(i+1)
    print('Linked List with duplicates:')    
    ll.printList()
    print('Length before deleting duplicate is: ', ll.length)
    ll.removeDupl_no_buf()
    ll.printList()
    print('Lenght after deleting duplicates is: ', ll.length)      


    ll = LinkList()
    l1 = [4, 2, 5, 7, 1, 9]
    for i in l1:
        ll.addInOrder(i)
    ll.printList() 
    print(ll.searchIfOrdered(7))       
    print(ll.searchIfOrdered(3))    
    ll.deleteNodeIfOrdered(7)
    ll.printList() 

    
if __name__ == '__main__':
    main()
