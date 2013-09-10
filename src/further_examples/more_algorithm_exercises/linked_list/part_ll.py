#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

''' This function partionate a linked list in a value, where everything smaller than this value
    goes to the front, and everything large goes to the back:'''

from linked_list_fifo import LinkList, Node
        
def partList(ll, n):
    more = LinkList()
    less = LinkList()
    node_old = ll.head
    while node_old:
        item = node_old.value
        if item < n:
            less.addNode(item)
        elif item > n:
            more.addNode(item)
        node_old = node_old.next
    
    less.addNode(n)
    nodemore = more.head
    while nodemore:
        less.addNode(nodemore.value)
        nodemore = nodemore.next  
    return less



def main():
    ll = LinkList()
    l1 = [6, 7, 3, 4, 9, 5, 1, 2, 8]
    for i in l1:
        ll.addNode(i)
    print('Before Part')    
    ll.printList()
    print('After Part')
    newll = partList(ll, 6)
    newll.printList()
   
                   
if __name__ == '__main__':
    main()

