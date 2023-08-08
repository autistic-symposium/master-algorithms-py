#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


class Stack:

    def __init__(self):
        self.content = []
        self.min_array = []
        self.min = float('inf')

    def __repr__(self):
        return f'{self.content}'

    @property
    def size(self):
        return len(self.content)
    
    @property
    def peek(self):
        if self.content:
            return self.content[-1]
        else:
            print('❌ Queue is empty, cannot peek.')
    
    @property
    def is_empty(self):
        return not bool(self.content)

    def push(self, value):
        if value < self.min:
            self.min = value

        self.content.append(value)
        self.min_array.append(self.min)
    
    def pop(self):
        if self.content:
            value = self.content.pop()
            self.min_array.pop()
            if self.min_array:
                self.min = self.min_array[-1]
            return value
    
    def find_min(self):
        if self.min_array:
            return self.min_array[-1]


if __name__ == '__main__':

    ######################
    #   Simple Stack
    ######################
    print('Testing Stack...')
    stack = Stack()
    for i in range(12, 21):
        stack.push(i)
    
    print(f'\nStack: {stack}')
    print(f'Stack size: {stack.size}')
    print(f'Stack peek: {stack.peek}')
    print(f'Stack is empty: {stack.is_empty}')
    print(f'Stack min: {stack.find_min()}')
    
    print('\nPopping...')
    for i in range(5):
        print(stack.pop())
    print(f'Stack: {stack}')
