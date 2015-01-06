#!/usr/bin/env python

__author__ = "bt3"


class HashTable(object):
    def __init__(self, slots=10):
        self.slots = slots
        self.table = []
        self.__create_table()

    def __hash_key(self, value):
        return hash(value)%self.slots

    def __create_table(self):
        for i in range(self.slots):
            self.table.append([])

    def add_item(self, value):
        key = self.__hash_key(value)
        self.table[key].append(value)

    def print_table(self):
        for key in range(len(self.table)):
            print "Key is %s, value is %s." %(key, self.table[key])



if __name__ == '__main__':
    dic = HashTable(5)
    for i in range(1, 40, 2):
        dic.add_item(i)

    dic.print_table()