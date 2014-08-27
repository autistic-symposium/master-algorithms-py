#!/usr/bin/python

__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"

''' Given a linked list, check if the nodes form a palindrome '''

from linked_list_fifo import LinkedListFIFO, Node
from node import Node

def isPal(l):

    if len(l1) < 2:
        return True
    if l1[0] != l1[-1]:
        return False

    return isPal(l1[1:-1])



def checkllPal(ll):
    node = ll.head
    l = []

    while node:
        l.append(node.value)
        node = node.pointer

    return isPal(l)





if __name__ == '__main__':

    ll = LinkedListFIFO()
    l1 = [1, 2, 3, 2, 1]

    for i in l1:
        ll.addNode(i)

    assert(checkllPal(ll) == True)

    ll.addNode(2)
    ll.addNode(3)

    assert(checkllPal(ll) == False)
