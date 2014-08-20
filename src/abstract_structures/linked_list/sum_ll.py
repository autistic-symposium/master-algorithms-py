#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

''' Supposing two linked lists represening numbers, such that in each of their 
    nodes they carry one digit. This function sums the two numbers that these
    two linked lists represent, returning a third list representing the sum:'''

from linked_list_fifo import Node, LinkList


def sumlls(l1, l2):
    lsum = LinkList()
    dig1 = l1.head
    dig2 = l2.head
    next = 0
    while dig1 and dig2:
        d1 = dig1.value
        d2 = dig2.value      
        sum_d = d1 + d2 + next
        if sum_d > 9:
            next = sum_d//10
            lsum.addNode(sum_d%10)
            
        else:   
            lsum.addNode(sum_d)
            next = 0
        
        dig1 = dig1.next
        dig2 = dig2.next
    
    if dig1:
        sum_d = next + dig1.value
        if sum_d > 9:
            lsum.addNode(sum_d%10)           
        else:   
            lsum.addNode(sum_d)   
        dig1 = dig1.next
    
    if dig2:
        sum_d = next + dig2.value
        if sum_d > 9:
            lsum.addNode(sum_d%10)           
        else:   
            lsum.addNode(sum_d)   
        dig2 = dig2.next    
    
    
    return lsum



def main():
    l1 = LinkList() # 2671
    l1.addNode(1)
    l1.addNode(7)
    l1.addNode(6)
    l1.addNode(2)
    
    l2 = LinkList() # 455
    l2.addNode(5)
    l2.addNode(5)
    l2.addNode(4)
    
    lsum = sumlls(l1, l2)
    lsum.printList()# 3126


if __name__ == '__main__':
    main()
