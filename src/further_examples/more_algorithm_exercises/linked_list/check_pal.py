#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

''' Given a linked list, check if the nodes form a palindrome '''

from linked_list_fifo import LinkList, Node

def isPal(l1):
    if len(l1) < 2: return True
    if l1[0] != l1[-1]: return False
    return isPal(l1[1:-1])

    
    
def checkllPal(ll):
    node = ll.head
    l1 = []
    while node:
        l1.append(node.value)   
        node = node.next
    return isPal(l1)  

        

def main():
    ll = LinkList()
    l1 = [1, 2, 3, 2, 1]
    for i in l1:
        ll.addNode(i)
    print(checkllPal(ll))
 
    ll.addNode(2)
    ll.addNode(3)
    print(checkllPal(ll))
    
                       
if __name__ == '__main__':
    main()

