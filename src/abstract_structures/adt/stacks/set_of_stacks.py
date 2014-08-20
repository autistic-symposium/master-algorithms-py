#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

class SetOfStacks(list):
    def __init__(self, capacity=4):
        self.stacks = []
        self.last_stack = []
        self.capacity = capacity
        self.stacks.append(self.last_stack)

    def __repr__(self):
        return str(self.stacks)

    def push(self, value):
        last_stack = self.last_stack
        if len(last_stack) is self.capacity:
            last_stack = []
            self.last_stack = last_stack
            self.stacks.append(last_stack)
        last_stack.append(value)

    def pop(self):
        last_stack = self.last_stack
        value = last_stack.pop()
        if len(last_stack) is 0:
            self.stacks.pop()
            self.last_stack = self.stacks[-1]
        return value


def main():
    stack = SetOfStacks()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    print(stack)
    stack.pop()
    stack.pop()
    stack.pop()
    print(stack)

if __name__ == '__main__':
    main()
