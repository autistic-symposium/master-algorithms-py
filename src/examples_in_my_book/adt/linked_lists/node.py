#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail


class Node(object):        
    def __init__(self, value):
        self.value = value
        self.next = None

    def getData(self):
        return self.value

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.value = newdata

    def setNext(self, newnext):
        self.next = newnext


