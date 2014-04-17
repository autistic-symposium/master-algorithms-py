#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

''' The first example design a Hash table using chaining to avoid collisions. The second 
    uses two lists.'''

from linked_list_fifo import Node, LinkList

class HashTableLL(object):
    def __init__(self, size):
        self.size = size
        self.slots = []
        self._createHashTable()

    def _createHashTable(self):
        for i in range(self.size) :
            self.slots.append(LinkList())
    
    def findIndex(self, item):
        return item%self.size

    def addItem(self, item):
        index = self.findIndex(item)
        self.slots[index].addNode(item)
        return self

    
    def delItem(self, item):
        index = self.findIndex(item)
        self.slots[index].deleteNode(item)
        return self


    def printHashTable(self):
        for i in range(self.size):
            print('\nSlot {}:'.format(i))
            print(self.slots[i].printList())
            
    

       

def test_hash_tables():
    H1 = HashTableLL(3)
    for i in range (0, 20):
        H1.addItem(i)
    H1.printHashTable()
    print('\n\nNow deleting:')
    H1.delItem(0)   
    H1.delItem(0)        
    H1.delItem(0) 
    H1.delItem(0) 
    H1.printHashTable()
'''
    H2 = HashTable2L(3)
    H2[54]="buffy"
    H2[26]="xander"
    H2[17]="giles"
    print(H.2slots)
'''


if __name__ == '__main__':
    test_hash_tables()       
