#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

class Stack(list):
    def push(self, value):
        if len(self) > 0:
            last = self[-1]
            minimum = self._find_minimum(value, last)
        else:
            minimum = value
        self.minimum = minimum
        self.append(NodeWithMin(value, minimum))

    def _find_minimum(self, value, last_value):
        if value < last_value.minimum:
           return value
        return last_value.minimum

    def min(self):
        return self.minimum


class NodeWithMin(object):
    def __init__(self, value, minimum):
        self.value = value
        self.minimum = minimum

    def __repr__(self):
        return str(self.value)

    def min(self):
        return self.minimum



def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    node = stack.pop()
    print(node.minimum)
    stack.push(0)
    stack.push(4)
    node = stack.pop()
    print(node.min())
    print(stack.min())
    print(stack)


if __name__ == '__main__':
    main()   


