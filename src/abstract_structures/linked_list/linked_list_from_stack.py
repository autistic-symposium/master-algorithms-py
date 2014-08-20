#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail



class Node(object):
	def __init__(self,data=None,next=None):
		self.data = data
		self.next = next
		
	def setnext(self,next):
		self.next = next
		
	def __str__(self):
		return "%s" % self.data


class LinkedListStack(object):
    ''' linked list from stack '''
    def __init__(self, max=0):
        self.max = max
        self.head = None
        self.z = None
        self.size = 0
        
    def push(self, data):
        if self.size == 0:
            self.head = Node(data=data)
            self.size += 1
        else:
            head = self.head
            temp = Node(data = data)
            self.head = temp
            self.head = temp
            temp.setnext(head)

    def pop(self):
        temp = self.head.next
        self.head = temp
        
    def isEmpty(self):
        return self.size == 0
            
    def __str__(self):
        d = ""
        if self.isEmpty(): return ""
        else:
            temp = self.head
            d += "%s\n" % temp
            while temp.next != None:
                temp = temp.next
                d += "%s\n" % temp
            return d
   
				
					
    
def test_ll_from_stack():
	ll = LinkedListStack(max = 20)
	ll.push("1")
	ll.push("2")
	ll.push("3")
	ll.push("4")
	print(ll)
	ll.pop()
	print(ll)
	

if __name__ == '__main__':
    test_ll_from_stack()
