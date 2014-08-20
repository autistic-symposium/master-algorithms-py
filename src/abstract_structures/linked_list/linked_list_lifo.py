#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail


''' Implement a unordered linked list, i.e. a LIFO linked list (like a stack) '''

class Node(object):
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class LinkList(object):
    def __init__(self):
        self.head = None
        self.lenght = 0
        
    def addNode(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.lenght += 1
        
    def printList(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next

    def deleteNode(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.next
            i += 1
        if index == i:
            self.lenght -= 1    
            if prev == None:
                self.head = node.next
            else:
                prev.next = node.next
        else:
            print('Node with index {} not found'.format(index))
         

    def deleteNodeByValue(self, item):
        prev = None
        node = self.head       
        found = False
        while node and not found:
            if node.value == item:
                found = True
            else:
                prev = node
                node = node.next
        if found:
            self.lenght -= 1 
            if prev == None:
                self.head = node.next
            else:
                prev.next = node.next
        else:
            print('Node with value {} not found'.format(item))


def main():
    ll = LinkList()
    for i in range(1, 11):
        ll.addNode(i)
    print('The list is:')
    ll.printList()
    print('The list after deleting node with index 2 (value 8):')
    ll.deleteNode(2)
    ll.printList()
    print('The list after deleting node with value 2 (index 7):')
    ll.deleteNodeByValue(2)
    ll.printList()

if __name__ == '__main__':
    main()
