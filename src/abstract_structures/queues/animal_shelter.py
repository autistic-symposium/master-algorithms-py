#!/usr/bin/python

__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"

""" A class for an animal shelter"""

class Node(object):
    def __init__(self, name, which):
        self.name = name
        self.which = which
        self.next = next
        self.timestamp = 0



class AnimalShelter(object):
    def __init__(self):
        self.first_cat = None
        self.first_dog = None
        self.last_cat = None
        self.last_dog = None
        self.counter = 0


    def enqueue(self, name, which):
        self.counter += 1
        node = Node(name, which)
        node.timestamp = self.counter

        if which == 'cat':
            if not self.first_cat:
                self.first_cat = node
            if self.last_cat:
                self.last_cat.next = node
            self.last_cat = node

        if which == 'dog':
            if not self.first_dog:
                self.first_dog = node
            if self.last_dog:
                self.last_dog.next = node
            self.last_dog = node



    def dequeueDog(self):
        if self.first_dog:
            node = self.first_dog
            self.first_dog = node.next
            return str(node.name)
        raise Exception('No Dogs!')



    def dequeueCat(self):
        if self.first_cat:
            node = self.first_cat
            self.first_cat = node.next
            return str(node.name)
        raise Exception('No Cats!')



    def dequeueAny(self):
        nodecat = self.first_cat
        nodedog = self.first_dog
        if nodecat and not nodedog:
            return self.dequeueCat()
        elif nodedog and not nodecat:
            return self.dequeueDog()
        elif nodedog and nodecat:
            if nodedog.timestamp < nodecat.timestamp:
                return self.dequeueDog()
            else:
                return self.dequeueCat()
        raise Exception('No Animals!')




def main():
    qs = AnimalShelter()
    qs.enqueue('bob', 'cat')
    qs.enqueue('mia', 'cat')
    qs.enqueue('yoda', 'dog')
    qs.enqueue('wolf', 'dog')

    assert(qs.dequeueDog() == 'yoda')
    assert(qs.dequeueCat() == 'bob')
    print(qs.dequeueAny() == 'mia')

if __name__ == '__main__':
    main()
