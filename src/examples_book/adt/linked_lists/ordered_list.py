#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail



from Node import Node

class OrderedList:
    """ The structure of an ordered list is a collection of items where each item 
    holds a relative position that is based upon some underlying characteristic of 
    the item. The ordering is typically either ascending or descending and we assume 
    that list items have a meaningful comparison operation that is already defined. 
    Many of the ordered list operations are the same as those of the unordered list. 
    """   
    def __init__(self):
        self.head = None


    def add(self,item):
        ''' this method is different from linked list '''
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
    
    
    def length(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count


    def search(self,item):
        ''' this method is different from linked list '''
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found


    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())



def test_OrderedList(module_name='this module'):
    olist = OrderedList()
    olist.add(31)
    olist.add(22)
    olist.add(10)
    assert(olist.search(22) == True)
    olist.remove(22)
    assert(olist.search(22) == False)   
    s = 'Tests in {name} have {con}!'
    print(s.format(name=module_name, con='passed'))


if __name__ == '__main__':
    test_OrderedList()


