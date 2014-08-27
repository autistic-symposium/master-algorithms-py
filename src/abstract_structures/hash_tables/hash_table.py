#!/usr/bin/python

__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"

''' design a Hash table using chaining to avoid collisions.'''


#import abstract_structures.linked_list.linked_list_fifo
#import abstract_structures.linked_list.node

from linked_list_fifo import LinkedListFIFO



class HashTableLL(object):
    def __init__(self, size):
        self.size = size
        self.slots = []
        self._createHashTable()

    def _createHashTable(self):
        for i in range(self.size) :
            self.slots.append(LinkedListFIFO())

    def _find(self, item):
        return item%self.size

    def _add(self, item):
        index = self._find(item)
        self.slots[index].addNode(item)

    def _delete(self, item):
        index = self._find(item)
        self.slots[index].deleteNode(item)

    def _print(self):
        for i in range(self.size):
            print('\nSlot {}:'.format(i))
            print(self.slots[i]._printList())




def test_hash_tables():
    H1 = HashTableLL(3)
    for i in range (0, 20):
        H1._add(i)
    H1._print()
    print('\n\nNow deleting:')
    H1._delete(0)
    H1._delete(1)
    H1._delete(2)
    H1._delete(0)

    H1._print()



if __name__ == '__main__':
    test_hash_tables()
